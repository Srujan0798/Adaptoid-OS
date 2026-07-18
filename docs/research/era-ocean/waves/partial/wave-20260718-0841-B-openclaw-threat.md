# ERA-OCEAN Partial B — OpenClaw Threat Model Deep Dive

| Field | Value |
|---|---|
| Wave | `wave-20260718-0841-B-openclaw-threat` |
| Agent | ERA-OCEAN partial **B** (OpenClaw security trench) |
| Category | Threat model · pairing · gateway security · main vs non-main sandbox · skills supply chain |
| Status | **PARTIAL / INCOMPLETE** — primary docs + SECURITY.md sampled; no local install, no `openclaw security audit` run, no formal-models TLC re-execution |
| Coverage honesty | Deep on documented trust boundaries and config surfaces; **not** a full code audit of `src/infra/exec-approvals*`, ClawHub scanner implementation, or live exposed-instance telemetry |
| Files written | **Only** this file |

---

## Mission question

What is OpenClaw’s **actual** security architecture (not marketing), and which **elite, portable concepts** should Adaptoid absorb into **OAP / FM-20** for agent product harnesses?

---

## 0. Incomplete honesty (read first)

| Gap | Impact |
|-----|--------|
| No local `openclaw security audit --deep` / live Gateway probe | Cannot claim current default posture of a fresh install beyond docs |
| Formal models live in **separate** repo (`vignesh07/openclaw-formal-models`); TLC not re-run | Claims are “docs-asserted green/red targets,” not session-verified |
| ClawHub scanner internals / moderation pipeline not reverse-engineered | Supply-chain residual risk is as **documented** (High/Critical), not independently measured |
| Secondary media (Cisco, Reddit, Semgrep cheatsheet, SlowMist guides) are **signals**, not primary truth | Use for residual-risk culture; prefer docs.openclaw.ai + SECURITY.md for policy |
| Community “~18k exposed instances / ~15% malicious skills” claims not re-measured here | Treat as **threat-intel rumor class** unless independently scanned |
| Adaptoid mapping is conceptual transfer, not a shipped patch | OAP/FM-20 deltas are recommendations for kit maintainers |

**What is solid:** official Security page, THREAT-MODEL-ATLAS, formal-verification page, sandboxing, skills, DM/node pairing, GitHub SECURITY.md triage policy.

---

## 1. Product shape that drives the threat model

OpenClaw is a **multi-channel personal-assistant Gateway**: messaging channels (WhatsApp, Telegram, Discord, Slack, Signal, …) feed an embedded agent that can run shell, filesystem, browser, network tools, cron, and paired **nodes** (mobile/desktop remote exec surfaces).

Security is therefore not “API auth for a SaaS chatbot.” It is **operator-delegated authority** on a host, reachable by anyone who can message the bot or call the Gateway WS/HTTP control plane.

Official stance (ordered):

1. **Identity first** — who may talk to the bot (DM pairing / allowlists / explicit open).
2. **Scope next** — where the bot may act (groups, tools, sandbox, device permissions).
3. **Model last** — assume the model can be manipulated; limit blast radius so manipulation is cheap to fail.

Most real failures are not exotic 0-days: *someone messaged the bot and the bot did what they asked.*

---

## 2. Foundational trust model (normative)

### 2.1 One trust boundary per Gateway

From [docs security](https://docs.openclaw.ai/gateway/security) + [SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md):

| Supported | Not supported / out of scope as “bug” |
|-----------|----------------------------------------|
| One user / trust domain per gateway (prefer one OS user / host / VPS) | Mutually untrusted/adversarial users sharing one gateway + config |
| Authenticated Gateway callers = **trusted operators** for that instance | Per-user multi-tenant isolation on one host |
| Config writers on `~/.openclaw` = trusted operators | “Missing per-user auth” on `sessionKey` |
| Separate gateway cells per tenant | Shared agent with tool authority among untrusted DMers |

Critical misread: `sessionKey` is a **routing selector**, not an authorization token. Shared-gateway “IDOR” on `sessions.list` / history is often **expected** in the personal-assistant model.

### 2.2 Gateway vs node as one operator domain

| Role | Job | Trust after auth/pair |
|------|-----|------------------------|
| **Gateway** | Control plane: auth, tool policy, routing, channel ingress | Full operator scope for shared-secret callers |
| **Node** | Remote execution surface (commands, device actions, host-local caps) | Paired node actions = **operator actions on that node** |

Exec approvals (allowlist + ask) are **operator-intent guardrails**, not hostile multi-tenant isolation. They bind exact request context and best-effort local operands — **not** a complete semantic model of every interpreter/loader path. Strong isolation requires sandboxing + OS/host split.

Default personal-assistant UX: host exec on gateway/node can be `security="full"`, `ask="off"` — intentional, not a vulnerability by itself.

### 2.3 What is deliberately **not** a vulnerability

SECURITY.md / security docs close as no-action (representative):

- Prompt-injection-only chains **without** policy/auth/approval/sandbox/tool-boundary bypass.
- Malicious plugin/skill **after** trusted operator install/enable (TCB extension).
- Operator-intended surfaces: TUI `!` shell, `canvas.eval`, browser evaluate, direct `node.invoke`.
- Shared-secret HTTP `/v1/chat/completions`, `/v1/responses`, `/tools/invoke` as full operator access (narrower `x-openclaw-scopes` **ignored** on shared-secret path).
- Public exposure / configs docs already recommend against.
- Parity-only heuristic gaps (obfuscation detection differences across exec paths) without boundary bypass.

**Implication for Adaptoid:** vulnerability triage and product security are different layers. Product DoD can still require defenses against prompt injection + supply chain even when upstream calls them “out of scope for GHSA.”

---

## 3. Official threat model (MITRE ATLAS + DFD)

Primary: [Threat model (MITRE ATLAS)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS) — **v1.0-draft**, living community doc. Scope includes agent runtime, Gateway, channels, **ClawHub**, MCP, partial user devices. Vulnerability-report scope truth is **SECURITY.md**, not the ATLAS page alone.

### 3.1 Trust boundaries (architecture)

```text
UNTRUSTED ZONE (WhatsApp / Telegram / Discord / …)
        │
        ▼
TB1 Channel Access — Gateway (pairing, AllowFrom, token/password/Tailscale)
        │
        ▼
TB2 Session Isolation — agent sessions (session key, tool policy, transcripts)
        │
        ▼
TB3 Tool Execution — Docker/host sandbox, node remote exec, SSRF controls
        │
        ▼
TB4 External Content — fetched URLs/emails/webhooks (wrapper markers)
        │
        ▼
TB5 Supply Chain — ClawHub (semver, SKILL.md, scanning, GH age)
```

Data flows F1–F6: channel→gateway→agent→tools/external/ClawHub→channel, with TLS/AllowFrom, session isolation, policy, SSRF, moderation, output filtering.

### 3.2 Critical threats (elite shortlist)

| ID | Tactic | Residual (docs) | Why it matters for harnesses |
|----|--------|-----------------|------------------------------|
| **T-EXEC-001** Direct prompt injection | Execution | **Critical** | Detection/wrapping only; PI out of scope for bugs without boundary bypass |
| **T-PERSIST-001** Malicious skill install | Persistence / supply chain | **Critical** | Skills run with agent privileges; no dedicated skill exec sandbox |
| **T-EXFIL-003** Credential harvest via skill | Collection | **Critical** | Env/config readable at agent privilege |
| **T-IMPACT-001** Unauthorized command execution | Impact | High/Critical | Sandbox **off by default**; host exec is deliberate default |
| **T-EXEC-002** Indirect PI (fetch/email) | Execution | High | Wrapper + notice; model may ignore |
| **T-EXEC-004** Exec approval bypass | Execution | High | Normalization helps; not complete semantics |
| **T-ACCESS-003** Token theft | Initial access | High | Secrets on disk; permissions primary control |
| **T-EXFIL-001** Exfil via web_fetch | Collection | High | Private nets blocked; arbitrary external OK |
| **T-ACCESS-001** Pairing code intercept | Initial access | Medium | 1h DM / 5m node TTLs |
| **T-PERSIST-002** Skill update poisoning | Supply chain | Medium–High | Auto-update race before review |

**Documented critical attack chains:**

1. Malicious skill → evade moderation → credential harvest  
2. Direct PI → exec approval bypass → host RCE  
3. Indirect PI via poisoned URL → web_fetch → external exfil  

### 3.3 Formal verification (bounded claims, not “proven secure”)

[Formal verification](https://docs.openclaw.ai/security/formal-verification): TLA+/TLC models for **highest-risk paths** under explicit assumptions. **Not** full TypeScript verification; model/code drift possible; green ≠ total security.

Documented claim clusters:

| Cluster | Positive targets (docs) | Negative (expected red) |
|---------|-------------------------|-------------------------|
| Gateway exposure | `gateway-exposure-v2`, `…-protected` | `…-negative` |
| Node exec pipeline + approval tokens | `nodes-pipeline`, `approvals-token` | matching negatives |
| Pairing store TTL/caps | `pairing`, `pairing-cap` | negatives |
| Ingress mention gating | `ingress-gating` | negative |
| Routing / session isolation | `routing-isolation` | negative |
| Pairing concurrency/idempotency | `pairing-race`, idempotency, refresh | race negatives |
| Ingress trace/idempotency | `ingress-trace*`, dedupe | negatives |
| dmScope precedence / identityLinks | `routing-precedence`, identitylinks | negatives |

Elite takeaway: OpenClaw invests in **machine-checked policy skeletons** for auth/pairing/routing — rare among agent harnesses. Adaptoid should note this as aspirational for OAP invariants, not as a substitute for runtime policy.

---

## 4. Pairing (two systems, often confused)

Primary: [Channel pairing](https://docs.openclaw.ai/channels/pairing), [Node pairing](https://docs.openclaw.ai/gateway/pairing).

### 4.1 DM pairing (who may talk)

| Policy | Behavior |
|--------|----------|
| **`pairing`** (default) | Unknown senders get code; **ignored until approve**. Code: 8-char unambiguous, **1h TTL**. Pending cap **3 per channel**. Repeat DMs don’t spam codes until new request |
| **`allowlist`** | Unknown blocked; no handshake |
| **`open`** | Public DMs only with explicit `allowFrom: ["*"]` opt-in |
| **`disabled`** | Ignore all inbound DMs |

```bash
openclaw pairing list <channel>
openclaw pairing approve <channel> <code>
```

**State:** SQLite `~/.openclaw/state/openclaw.sqlite` (`channel_pairing_requests`, `channel_pairing_allow_entries`). Legacy JSON under `credentials/` migrates via doctor.

**First owner bootstrap:** first DM pairing approval can set `commands.ownerAllowFrom` when no owner exists. Later pairings grant DM access only — **not** automatic group command rights.

**Groups are separate:** group allowlists + `requireMention` + `groupAllowFrom`. Reply-as-mention does **not** bypass `groupAllowFrom`.

**Session isolation vs auth:**

| `session.dmScope` | Effect |
|-------------------|--------|
| `main` (default) | All DMs share one rolling main session (personal-agent default) |
| `per-channel-peer` | Isolated DM context per channel+sender (**secure multi-user messaging**) |
| `per-account-channel-peer` | Further split by account |
| `per-peer` | One session per sender across channels of same type |

Messaging isolation ≠ host isolation. Multi-user inbox → set isolating `dmScope`; adversarial users → **separate gateways**.

**Context visibility** (`contextVisibility`) is separate from trigger auth: can filter quoted/thread context from non-allowlisted senders (`all` | `allowlist` | `allowlist_quote`).

### 4.2 Device + node pairing (who may join the control plane)

Two layers on the same paired-device record:

1. **Device pairing** (`role: node` / operator / browser) — gates **connect** handshake.
2. **Node capability approval** (`node.pair.*`) — gates which **declared commands/caps** a connected node may expose.

Breaking change (2026.3.31+ docs): **device pairing alone is not enough** for node commands; node capability pairing must be approved or commands stay filtered. Commands queued before approval are **dropped**, not deferred.

Pending capability requests: expire **5 minutes after last retry** (reconnects refresh rather than spawning infinite pending prompts).

```bash
openclaw devices list | approve | reject
openclaw nodes pending | approve | reject | status | remove
```

**Approval scopes (node.pair.approve):**

| Request surface | Needed operator scopes (docs) |
|-----------------|-------------------------------|
| Commandless | `operator.pairing` |
| Ordinary commands | `operator.pairing` + `operator.write` |
| Admin-sensitive (`system.run`, browser.proxy, fs.listDir, execApprovals…, etc.) | `operator.pairing` + `operator.admin` |

**Important:** pairing records trusted **capability surface** but live commands are still filtered by **global** `gateway.nodes.allowCommands` / `denyCommands`. Per-node `system.run` ask/allow lives in `exec.approvals.node.*` on the node — not a second hidden per-command pairing layer.

### 4.3 Auto-approval paths (high blast-radius if misunderstood)

| Mechanism | Default | Safety claim (docs) |
|-----------|---------|---------------------|
| **SSH-verified node auto-approve** | **On** | Gateway SSHes back (`BatchMode`, strict host keys), runs `openclaw node identity --json`, approves only on **exact device-key match**. Reachability alone never approves. Private/CGNAT (+ optional cidrs). Fail → normal prompt |
| **Trusted-CIDR auto-approve** | **Off** | Explicit CIDRs only; fresh scopeless `role: node` only; never operator/browser/Control UI; never upgrades/key changes |
| **Loopback local device** | Auto for true loopback | Forwarded-header evidence **disqualifies** loopback locality (anti spoof) |
| **Metadata-upgrade auto** | Narrow | Local non-browser only; scope/key upgrades still manual |
| **QR/setup codes** | Manual issue | Bootstrap token ~10m; plaintext `ws://` limited; full access needs `wss://` / Tailscale Serve |

Device tokens in SQLite are **secrets**. Rotate via `openclaw devices rotate` / `device.token.rotate`.

### 4.4 Elite pairing concept for Adaptoid

OpenClaw separates:

- **Identity admission** (pairing/allowlist)
- **Capability surface expansion** (pending upgrade requests, never silent widen)
- **Runtime policy** (global node command policy + exec approvals)
- **Locality claims** (loopback only if socket **and** proxy headers agree)

Adaptoid OAP should mirror **admission ≠ capability ≠ continuous policy**, and treat “scope upgrade” as a first-class approval event (FM-18/FM-20).

---

## 5. Gateway security

Primary: [Security](https://docs.openclaw.ai/gateway/security), exposure runbook, audit checks.

### 5.1 Default posture goals

Hardened baseline (docs “60 seconds”):

- `gateway.mode: local`, `bind: loopback`, `auth.mode: token` (long random)
- `session.dmScope: per-channel-peer` when multi-user messaging
- Tools: messaging profile; deny automation/runtime/fs/session spawn groups; `fs.workspaceOnly`; `exec.security: deny` + `ask: always`; elevated off
- Channels: pairing + group `requireMention`

Even loopback: onboarding generates a token so local WS clients must authenticate. Auth required fail-closed when no valid path configured.

### 5.2 Network exposure matrix (mental model)

| Surface | Risk class | Notes |
|---------|------------|-------|
| Bind `loopback` | Baseline | Preferred |
| Bind `lan` / custom / public | High | Auth + firewall mandatory; never unauth `0.0.0.0` |
| Tailscale Serve | Preferred remote | Gateway stays loopback; Tailscale handles edge |
| Tailscale Funnel / public | Highest | Treat as last resort; audit immediately |
| Docker published ports | Host firewall bypass class | DOCKER-USER chain must deny by default |
| Bonjour/mDNS full mode | Recon aid | Prefer `minimal`/`off`; full leaks `cliPath`/`sshPort` |
| Control UI canvas (`/__openclaw__/canvas`) | Untrusted HTML/JS | Don’t co-origin with privileged web |

Default port **18789** (WS+HTTP multiplex).

### 5.3 Auth modes

| Mode | Meaning |
|------|---------|
| `token` | Shared bearer (recommended) |
| `password` | Prefer env `OPENCLAW_GATEWAY_PASSWORD` |
| `trusted-proxy` | Identity-aware reverse proxy headers; strict loopback rules |
| Tailscale Serve identity | Optional `allowTailscale`; verifies via local `tailscale whois`; **not** for HTTP API `/v1/*` |

**Shared-secret HTTP is full operator access:** `/v1/chat/completions`, `/v1/responses`, `/tools/invoke` restore full operator scopes + owner semantics; narrower `x-openclaw-scopes` does **not** reduce shared-secret path. Only identity-bearing modes honor per-request scopes.

### 5.4 Reverse proxy / locality hardening

- `gateway.trustedProxies` required for honest client IP; untrusted XFF → not local.
- Proxies must **overwrite** XFF, not append client-supplied chains.
- Loopback + forged `X-Forwarded-*` → **not** treated as same-host auto-trust for pairing.
- Control UI needs secure context; `allowInsecureAuth` / `dangerouslyDisableDeviceAuth` are audited dangerous flags.

### 5.5 `openclaw security audit`

```bash
openclaw security audit
openclaw security audit --deep   # live Gateway probe
openclaw security audit --fix
openclaw security audit --json
```

Checks (high level): inbound DM/group openness, tool blast radius, exec/fs drift, network bind/auth, browser remote exposure, disk permissions, plugins without allowlist, sandbox mode off while docker configured, skills supply-chain prefixes, model hygiene.

Triage priority (docs): open+tools → public exposure → browser remote → permissions → plugins → model tier.

`--fix` is intentionally narrow (open groups→allowlists, redactSensitive, chmod/ACLs) — not a full harden-to-minimal tools rewrite.

### 5.6 Secrets & host hygiene

Assume entire `~/.openclaw/` is sensitive: config tokens, channel creds, SQLite (device tokens, MCP OAuth), session transcripts, sandboxes copies.

- Dir `700`, files `600`; full-disk encryption; dedicated OS user if host shared.
- Workspace `.env` **cannot** override provider keys or `OPENCLAW_*` runtime namespace (fail-closed).
- SecretRefs / secrets plan contract for additive secret management.
- Transcripts on disk = trust boundary is filesystem access.

### 5.7 Prompt injection as product reality

Docs are unusually honest: PI **not solved** by system prompts. Hard enforcement = tool policy, exec approvals, sandbox, channel allowlists (all operator-disableable by design).

Indirect PI surfaces: web fetch/search, browser, email hooks, attachments, OpenResponses URL inputs, media-understanding text extraction.

Mitigations of note:

- External content wrapping with **random-boundary** markers + security notice; chat-template special-token sanitization for self-hosted backends.
- Outbound reply sanitizer strips leaked tool/system scaffolding.
- Reader-agent pattern: untrusted summarize → handoff to main with restricted `tools.agentToAgent`.
- Browser SSRF private-network blocked by default; navigation preflight imperfect (docs admit request-level, not full network firewall).
- Model tier: **do not** put tool-enabled / untrusted-inbox agents on weak models.

---

## 6. Sandbox: `off` | `non-main` | `all` (main vs non-main)

Primary: [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing).

### 6.1 What is sandboxed

| Sandboxed when enabled | Never sandboxed |
|------------------------|-----------------|
| Tool execution: exec, read, write, edit, apply_patch, process, … | **Gateway process** itself |
| Optional sandboxed browser | Tools with `tools.elevated` escape path |

**Default: `agents.defaults.sandbox.mode = off`.** Host-first trusted-operator model. `tools.exec.host` default `auto`: sandbox when active for session, else gateway.

Docs warning: not a perfect security boundary, but material FS/process limit when model misbehaves.

### 6.2 Mode semantics (the “main” distinction)

| Mode | When sandbox applies |
|------|----------------------|
| **`off`** | Never |
| **`non-main`** | Every session **except** the agent’s **main** session |
| **`all`** | Every session |

**Main session key is fixed:** `agent:<agentId>:main` (or `global` when `session.scope` is `"global"`). Not configurable. Group/channel sessions use other keys → always non-main → sandboxed under `non-main`.

**Product intent:** personal “main” chat keeps full host power for owner UX; satellite sessions (groups, secondary peers, non-main keys) get containment. This is a **convenience isolation** pattern, not multi-tenant security — a prompt-injected main session still owns the host if sandbox is off or elevated is used.

### 6.3 Scope & backend

| Setting | Values | Default |
|---------|--------|---------|
| Scope | `agent` \| `session` \| `shared` | `agent` |
| Backend | `docker` \| `ssh` \| `openshell` | `docker` |

Docker defaults (when on): `network: "none"`, `readOnlyRoot: true`, `capDrop: ["ALL"]`, image `openclaw-sandbox:bookworm-slim`. Host/network namespace join blocked by default.

**Workspace access:** `none` (isolated sandbox workspace) | `ro` (`/agent`) | `rw` (`/workspace`). Skills mirrored into sandbox read paths depending on access.

**Elevated:** bypasses sandbox onto gateway/node — intentional escape hatch.

### 6.4 Policy drift (audit-critical)

Security audit flags:

- Docker sandbox settings present but `mode: off`
- Expecting implicit exec = sandbox while `host=auto` resolves to gateway when sandbox inactive
- Explicit `host=sandbox` while mode off → **fail closed** (no runtime)

### 6.5 Adaptoid transfer

Map OpenClaw modes → product profiles:

| OpenClaw | Adaptoid-ish profile |
|----------|----------------------|
| `off` + owner main | **Trusted operator interactive** (local coding) |
| `non-main` | **Owner full / others contained** (messaging multi-room) |
| `all` + workspace `ro`/`none` | **Untrusted content / public bot** |
| Elevated | **Break-glass** (must be logged + rare) |

OAP should encode sandbox **mode** as a pre-tool predicate, not only tool name allowlists.

---

## 7. Skills supply chain

Primaries: [Skills](https://docs.openclaw.ai/tools/skills), ATLAS §4 ClawHub, SECURITY.md trusted plugins.

### 7.1 What a skill is (security-relevant)

Skills are **markdown instruction packages** (`SKILL.md` + optional assets) that teach the agent how/when to use tools. They load into agent prompt/catalog; they are **not** a separate least-privilege runtime by default. ATLAS residual: *skills run with agent privileges; no execution sandboxing for skills at runtime.*

Load precedence (highest first): workspace → project agent → personal agent → managed `~/.openclaw/skills` → bundled → extraDirs/plugins.

Node-hosted skills appear while node connected; collisions get node-prefixed names; exec via `host=node`.

### 7.2 Controls that exist

| Control | Mechanism | Limit |
|---------|-----------|-------|
| Agent skill allowlist | `agents.defaults.skills` / per-agent list | Visibility only — not shell auth if exec remains open |
| Path containment | Realpath must stay in skill root (symlink rules) | Trusted operator can still allow symlink targets |
| Install policy hook | `security.installPolicy` local command, fail-closed | Operator-defined quality |
| ClawHub verify | `openclaw skills verify` trust envelope | Registry-dependent |
| ClawHub scans | Static/AST-adjacent, LLM agentic review, VirusTotal, GH account age ≥14d | Pattern/LLM bypass residual **High** |
| Skill Workshop | Proposal queue; human apply | Process, not crypto boundary |
| Env injection | Per-run host env for skill keys | Host process; **not** sandbox |
| Uploaded zip install | Off by default (`allowUploadedArchives`) | High-risk path if enabled |
| Snapshotting | Session-start skill set; refresh on watch/node | Mid-session changes need next turn |

`requires.bins` checked on **host** at load; sandbox containers need bins installed separately (`setupCommand` / custom image).

### 7.3 ClawHub moderation (docs matrix)

Strengths: path sanitization, size caps (~50MB), text-file bias, multi-layer scanning, badges/reporting.

Known gaps (ATLAS):

- Novel obfuscation / dynamic load evasion  
- LLM/VT depend on operator API keys  
- **No runtime skill isolation** from agent privilege  
- Update poisoning residual if auto-update races review  

Critical chain: publish skill → evade scan → harvest credentials / steer tools.

### 7.4 Plugins = TCB

SECURITY.md: enabling a plugin grants **same trust as local code** on the gateway host. Reports that only show “malicious plugin after install” are out of scope. Product security must treat plugin/MCP/skill install as **privilege grant** events (Adaptoid FM-20).

### 7.5 Community residual risk (secondary, unmeasured)

Public discourse (2026) flags: large exposed-instance populations, unreviewed community skills, “no perfectly safe setup” language in product docs. Cisco-class commentary: security is configurable, high privilege is the product. Use as **operational stress**, not as measured CVE density in this wave.

---

## 8. Elite concepts for Adaptoid (OAP + FM-20)

Adaptoid already has:

- **OAP** — fail-closed pre-tool-call policy (`ALLOW` / `DENY` / `REQUIRE_APPROVAL`) — [`protocols/oap-security.md`](../../../../../protocols/oap-security.md)
- **FM-20** — MCP/tool trust & injection — [`failure-modes/FM-20-mcp-tool-trust.md`](../../../../../failure-modes/FM-20-mcp-tool-trust.md)
- **FM-18** — unauthorized tool / destructive action

### 8.1 Portable imports (high value)

| OpenClaw concept | Adaptoid adoption sketch |
|------------------|--------------------------|
| **Identity → Scope → Model** ordering | Product security docs + SDLC gate order: never “prompt harden first” |
| **One trust boundary per host/user** | Generated projects: forbid multi-tenant claims on one agent cell |
| **Pairing admission vs capability upgrade** | OAP events: `ADMIT`, `SCOPE_UPGRADE`, `TOOL_INVOKE` as distinct |
| **Shared-secret = full operator** honesty | Document MCP/HTTP bridge credentials as r3+; no fake fine-grained scopes on bearer |
| **sessionKey is routing, not auth** | Session IDs never appear as “tenancy” in DoD |
| **`non-main` sandbox pattern** | Profiles: owner interactive vs untrusted room vs CI sandbox |
| **security audit with checkIds** | Ship `validators`/`oap_security.sh` structured findings, not only green/red scripts |
| **External content wrappers** | Treat MCP tool results, web fetch, email as `EXTERNAL_UNTRUSTED` in Brain prompts |
| **Reader agent / tool-disabled summarizer** | Pattern for untrusted inputs before Hands tools |
| **Install policy fail-closed** | No auto marketplace MCP/skills in generated projects (already FM-20) |
| **Dangerously\* flags explicit** | Config schema: break-glass names must be greppable and audited |
| **Formal models for policy skeletons** | Optional future: TLA or property tests for OAP precedence (deny-by-default) |
| **Plugins/skills = TCB** | Pin hashes/versions; treat description text as untrusted (FM-20) |
| **dmScope multi-user isolation** | If Adaptoid ever multi-peer messaging, default isolate sessions |
| **Exec approvals ≠ sandbox** | OAP approval is not isolation; map to host sandbox profiles (SHIP-SYSTEM) |

### 8.2 FM-20 refinements suggested by OpenClaw

1. **MCP/shell asymmetry:** OpenClaw docs and Adaptoid SHIP-SYSTEM both note host sandbox may not cover all tool planes (Codex: shell sandboxed, MCP often not). FM-20 recovery should require **separate** MCP egress policy.  
2. **Skill/MCP install = privilege grant** — log + human for write/network servers (blast-radius r3).  
3. **Verify envelope** analog — prefer pin + signature/checksum over “downloaded from marketplace.”  
4. **Update poisoning** — pin versions; no silent `update --all` in production agents.  
5. **Prompt injection residual is product risk** even if GHSA-out-of-scope — acceptance tests should include PI→tool attempts under OAP deny.

### 8.3 OAP policy pack deltas (concept only)

```yaml
# Conceptual — not a repo change this wave
skills_mcp:
  default: DENY
  install: REQUIRE_APPROVAL
  invoke_network: REQUIRE_APPROVAL
  invoke_host_exec: REQUIRE_APPROVAL
  invoke_readonly_local: ALLOW  # only if server pinned + allowlisted

session_scopes:
  main_owner: tools.elevated possible
  non_main: sandbox=all + deny elevated
  public_room: tools=messaging-only
```

### 8.4 What **not** to copy blindly

| OpenClaw default | Why Adaptoid may differ |
|------------------|-------------------------|
| Sandbox **off** by default | Agent-product archetype may prefer sandbox-on for untrusted workspaces |
| `security=full` / `ask=off` host exec | Coding harness UX vs autonomous messaging bot risk |
| Personal-assistant multi-tenant non-goal | Enterprise multi-user products need stronger tenancy (separate cells) |
| PI out of GHSA scope | Product compliance still owns PI residual risk |

---

## 9. Hardened operator checklist (condensed)

1. `bind: loopback` + long token; remote only via Tailscale Serve/`wss`.  
2. `dmPolicy: pairing` or allowlist; never open without `*`. Groups: mention + allowlists.  
3. Multi-person DMs → `dmScope: per-channel-peer`.  
4. Prefer `sandbox.mode: all` for tool-enabled untrusted content; `non-main` only if main is truly owner-only.  
5. Minimal tools profile; deny automation/runtime/fs until needed; elevated off.  
6. Strong latest-generation model for any tool-enabled agent.  
7. Skills/plugins: allowlist per agent; verify ClawHub; read SKILL.md; pin versions; installPolicy if available.  
8. Browser: dedicated profile; SSRF strict; no public browser control.  
9. `openclaw security audit --deep` after every exposure change; doctor for pairing drift.  
10. Separate OS user/VPS per trust domain; encrypt disk; 700/600 on state.

---

## 10. Sources

### Primary (authoritative for this note)

| Source | URL |
|--------|-----|
| Security (gateway) | https://docs.openclaw.ai/gateway/security |
| Threat model ATLAS | https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS |
| Formal verification | https://docs.openclaw.ai/security/formal-verification |
| Sandboxing | https://docs.openclaw.ai/gateway/sandboxing |
| Configuration (sandbox modes) | https://docs.openclaw.ai/gateway/configuration |
| Skills | https://docs.openclaw.ai/tools/skills |
| Channel pairing | https://docs.openclaw.ai/channels/pairing |
| Node pairing | https://docs.openclaw.ai/gateway/pairing |
| SECURITY.md | https://github.com/openclaw/openclaw/blob/main/SECURITY.md |
| Formal models repo | https://github.com/vignesh07/openclaw-formal-models |
| Trust / disclosure (referenced) | https://trust.openclaw.ai · openclaw/trust |

### Secondary (context / culture; not policy)

| Source | Role |
|--------|------|
| Semgrep OpenClaw security cheat sheet | Engineer operational checklist |
| DefectDojo OpenClaw hardening checklist | Config checklist mirror of docs |
| Cisco blog on personal AI agents | Residual-risk narrative |
| Reddit/community skill risk threads | Unverified skill malware rates |
| SlowMist OpenClaw security practice guide | High-privilege agent practice guide |

### Adaptoid internal anchors

| Path | Role |
|------|------|
| `protocols/oap-security.md` | OAP fail-closed pre-tool |
| `failure-modes/FM-20-mcp-tool-trust.md` | MCP/tool trust FM |
| `failure-modes/FM-18-unauthorized-tool.md` | Unauthorized tool FM |
| `core/SHIP-SYSTEM.md` | Sandbox/MCP blast-radius product surface |
| `docs/research/era-ocean/elite/ELITE-10-PERCENT.md` | Elite connector/MCP notes |

---

## 11. Bottom line

OpenClaw’s security story is **coherent and unusually well-documented** for agent harnesses: a **personal trusted-operator** model, layered **pairing**, a serious **Gateway exposure** story, optional **Docker/SSH sandboxes** with a sharp **main vs non-main** split, and an explicit **ClawHub supply-chain residual** (Critical on malicious skills). It does **not** claim multi-tenant safety or solved prompt injection.

For Adaptoid **OAP/FM-20**, the elite imports are: **admission vs capability vs continuous policy**, **honest full-operator secrets**, **sandbox profiles by session class**, **install-as-privilege-grant**, **external-content quarantine**, and **structured security audit** — not OpenClaw’s default of host-exec-on-main with sandbox off.

---

## 12. Residual open questions (next waves)

1. Re-run TLC targets in `openclaw-formal-models` and archive green/red logs.  
2. Local `openclaw security audit --json` on a clean onboard for baseline checkId set.  
3. ClawHub scan false-negative study (controlled skill samples) — optional red-team wave.  
4. Compare OAP packs vs OpenClaw `tools.profile` + deny groups for mechanical mapping.  
5. Node `denyCommands` exact-ID-only pitfall — write Adaptoid doc trap if we ever expose remote nodes.
