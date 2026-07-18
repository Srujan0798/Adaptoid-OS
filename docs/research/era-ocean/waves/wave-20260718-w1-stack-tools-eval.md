# Wave 2026-07-18 W1 — Stack, tools, deploy, eval (official-docs lens)

| Field | Value |
|---|---|
| Wave | `wave-20260718-w1-stack-tools-eval` |
| Category | Tools / backends / DBs / deploy + benchmarks / evals + MCP + agent CI |
| Lens | Official docs + production relevance (not hype ranking) |
| Status | Draft research — ocean open |
| Coverage honesty | ≪1% of stack surface; top ~10 per category by elite-agent fit |

## Mission question

What should an **agent harness** (Adaptoid-class) encode as **default stack hints** vs what must stay **never hardcode** — so generated projects ship with proven infrastructure patterns without locking vendors?

---

## North-star rule (harness encoding)

| Encode as **default stack hints** | **Never hardcode** |
|---|---|
| Capability *shape* (edge HTTP, long-running worker, durable state, vector memory, OTEL traces, golden evals) | Vendor brand as the only path |
| Interfaces (Postgres wire, Redis protocol, OpenTelemetry, OAuth resource server, GitHub Actions YAML) | Region, pricing tier, exact SaaS plan |
| Security defaults (MCP allowlist, deny-by-default tools, no token passthrough, SSRF blocks) | Specific MCP marketplace servers |
| Eval *discipline* (pass@k, golden tasks, offline + online, cost/step caps) | Single public leaderboard as product KPI |
| CI gates that are deterministic (lint, type, unit, ship-check) | Autonomous agent commit-to-main without human gate |
| Smallest viable stack for archetype (matches Core `pull_ecosystem`) | Full SaaS suite on every scaffold |

**Adaptoid mapping today:** `adaptor/engine.py` `pull_ecosystem` already prefers brief-derived `stack_hints` (python/node/react/postgres) and archetype backends (`fastapi`, `node`) — correct direction. Extend with *capability tags*, not vendor IDs.

---

## 1. Deploy / edge

### Top production-relevant platforms (~10)

| # | Platform | Why elite agents use it | Official signal |
|---|---|---|---|
| 1 | **Vercel** (+ AI SDK) | Front-door for streaming agent UIs; AI SDK `ToolLoopAgent` / harness adapters; deploy with one push | [AI SDK Agents](https://ai-sdk.dev/docs/agents/overview) |
| 2 | **Cloudflare Workers + Agents** | Durable identity, SQLite-backed state, WebSockets, schedule, sandbox, MCP tools on global edge | [Cloudflare Agents](https://developers.cloudflare.com/agents/) |
| 3 | **Fly.io** (Machines / Sprites) | Isolated VMs, private FS, good for untrusted code + long agent runtimes | [Fly.io](https://fly.io/) (Sprites agent env) |
| 4 | **Railway** | Agent-native ops: CLI + local/remote MCP + agent skills for deploy/logs/vars | [Railway for Agents](https://docs.railway.com/agents) |
| 5 | **Render** | Web + background workers + managed Postgres/pgvector + Key Value; simple prod path | [Render Postgres](https://render.com/docs/postgresql), AI agent guides |
| 6 | **AWS / GCP / Azure** (baseline) | Enterprise default when compliance/network isolation dominates | (vendor clouds; not agent-specialized) |
| 7 | **Modal / RunPod / GPU hosts** | Burst GPU for embed/train/eval jobs, not always for chat path | workload-specific |
| 8 | **Kubernetes + containers** | Team already k8s-native; portable worker fleets | portable contract > cluster brand |
| 9 | **Deno Deploy / Netlify** | Edge TS niche; less agent-runtime depth than CF/Vercel | secondary |
| 10 | **Self-host Docker Compose** | Offline / airgap / cost ceiling; matches T1–T2 local truth | always keep as escape hatch |

### Per-platform: encode vs never hardcode

| Platform | **Default stack hints** | **Never hardcode** |
|---|---|---|
| Vercel | `edge_http`, `streaming_ui`, `ai_sdk_tool_loop`, serverless function timeout awareness | “Must deploy on Vercel”; specific region; AI Gateway as only model path |
| Cloudflare | `durable_agent_runtime`, `edge_state_sqlite`, `websocket_session`, `sandbox_tool`, MCP tool surface | Workers AI as only model; DO class names; account IDs |
| Fly | `vm_isolation`, `long_running_process`, `private_filesystem`, agent sandbox pattern | Machine size; org; “Sprites-only” |
| Railway | `paas_deploy`, `agent_mcp_ops`, env/var/log tooling for agents | Project IDs; MCP remote as sole auth path |
| Render | `web_plus_worker`, `managed_postgres`, `redis_compatible_kv`, blueprint deploy | Service plan; single Blueprint as architecture |
| Big cloud | `vpc`, `iam`, `secrets_manager`, `private_network` | Specific service names in kernel |
| Compose | `local_repro`, `docker_up`, offline-first | Forbidding cloud forever |

### Harness takeaway

- Hint **runtime class**: `request_short` | `edge_durable` | `vm_long` | `worker_queue` — then let human/brief pick vendor.
- Agents that **mutate deploy state** (Railway MCP, cloud CLIs) are **high blast-radius** (FM-20): require allowlist + human gate in harness policy.

---

## 2. Backend / API

### Top production-relevant backends (~10)

| # | Stack | Role for agent products |
|---|---|---|
| 1 | **FastAPI** (Python) | Agent APIs, tool servers, eval runners; already Core internal-tool default |
| 2 | **Next.js** (App Router) | Full-stack TS product surface + AI SDK streaming |
| 3 | **Vercel AI SDK** (TS) | Model-agnostic tool loop, MCP tools, policy tool approvals, telemetry hooks |
| 4 | **tRPC** | Type-safe BFF when monorepo TS; not agent-specific |
| 5 | **Supabase** | Auth + Postgres + realtime + storage BaaS; agent memory tables |
| 6 | **Firebase** | Mobile/realtime BaaS; weaker “agent OS” fit than Supabase/Postgres |
| 7 | **Hono / Express / Nest** | Lightweight or enterprise Node APIs |
| 8 | **Django / Rails** | Legacy product wrap; agent as sidecar |
| 9 | **gRPC / Connect** | Internal multi-service agent fleets |
| 10 | **Serverless functions only** | Fine for thin tool endpoints; bad sole home for long agent loops |

### Encode vs never hardcode

| Hint | Encode | Never hardcode |
|---|---|---|
| Language | `python` / `typescript` from brief | “Always Python” |
| API style | REST or RPC + OpenAPI contract | Framework fashion of the week |
| Agent loop host | Separate long-lived process vs edge DO vs queue worker | Forcing loop inside 10s serverless |
| Auth | OIDC/session + service tokens for tools | Firebase-only or Supabase-only |
| Streaming | SSE/WebSocket first-class | Ignoring disconnect/resume |
| Tool surface | Schema-validated tools (Zod/Pydantic) | Free-form shell as default tool |

**Official anchors:** AI SDK defines agents as *LLM + tools + loop* with stop conditions and runtime context — harness should speak that vocabulary regardless of framework.

---

## 3. Databases & agent memory

### Top production-relevant data systems (~10)

| # | System | When agents need it |
|---|---|---|
| 1 | **PostgreSQL** | System of record: sessions, audit, tasks, users — always first |
| 2 | **pgvector** (on Postgres) | Embeddings + metadata filters without second vendor; Render/Neon/Supabase common |
| 3 | **Neon** (serverless Postgres) | Branching DB for previews/eval; scale-to-zero |
| 4 | **Supabase Postgres** | Same as PG + product auth/realtime |
| 5 | **Redis / Valkey** | Ephemeral state, rate limits, queues, session cache |
| 6 | **PlanetScale** / MySQL-compatible | Product DBs already MySQL; not vector-first |
| 7 | **Qdrant** | Dedicated vector when filter+latency+scale outgrow pgvector |
| 8 | **Pinecone** | Fully managed vector; multi-namespace agent memory at scale |
| 9 | **Cloudflare D1 / DO SQLite / Vectorize** | Edge-local agent state (with CF Agents runtime) |
| 10 | **Object storage (S3/R2)** | Artifacts, traces blobs, tool outputs — not a substitute for rows |

### Memory pattern (elite practice)

1. **Transactional memory** → Postgres (facts, approvals, audit).
2. **Semantic memory** → pgvector first; promote to Qdrant/Pinecone when scale/SLA demands.
3. **Working memory** → Redis or in-process with explicit TTL.
4. **Durable agent identity** → DO/SQLite or VM disk only when runtime co-located (CF/Fly).

### Encode vs never hardcode

| Encode | Never hardcode |
|---|---|
| `database: postgres` as default system of record | Neon vs RDS vs Supabase as kernel constant |
| `vector: pgvector | dedicated` capability flag | Pinecone/Qdrant as only memory |
| Migration discipline, backup/PITR requirement | “Memory = vector DB” without relational audit |
| Multi-tenant isolation keys (`tenant_id`, agent_id) | Single global index for all users |
| Embed model + dimension as **config**, not code constants | One embed model forever in templates |

---

## 4. Observability for agents

### Top platforms (~ production relevance)

| # | Tool | Strength | Official lens |
|---|---|---|---|
| 1 | **Langfuse** | OSS, self-host, OTEL-native, traces/sessions/agent graphs, prompts, evals | [Langfuse docs](https://langfuse.com/docs) |
| 2 | **LangSmith** | Deep LangChain/LangGraph + multi-framework; traces, online eval, dashboards | [LangSmith Observability](https://docs.langchain.com/langsmith) |
| 3 | **Arize Phoenix** | OSS OTEL/OpenInference; tracing + datasets/experiments + eval rigor | [Phoenix docs](https://arize.com/docs/phoenix) |
| 4 | **Helicone** | Drop-in gateway/proxy logging, multi-model, low install friction | [Helicone quickstart](https://docs.helicone.ai/) |
| 5 | **Datadog / Honeycomb LLM** | Enterprise shops already on APM | secondary for pure agent startups |
| 6 | **OpenTelemetry alone** | Vendor-neutral transport; required interoperability layer | industry convergence |
| 7 | **Cloudflare / platform logs** | Runtime metrics where agent is hosted | complement, not replace LLM traces |
| 8 | **Custom score APIs** | Product-specific graders posted to any backend | always available escape |

### Encode vs never hardcode

| Encode as default | Never hardcode |
|---|---|
| **OpenTelemetry** (or equivalent span model): generation, tool, retrieval, agent step | Langfuse *or* LangSmith as sole SDK in kernel |
| Trace IDs on every agent run; session/user correlation | Shipping agent product with zero LLM observability at T2 |
| Cost + latency + token metrics as first-class | Only “vibe check” dashboards |
| Prompt version linking to traces | Prompt strings only in code with no version |
| Eval scores attached to spans | Vendor-specific score UI as acceptance criterion |

**Harness rule:** Prefer **OTEL export config** in generated projects; document optional backends (Langfuse self-host, LangSmith cloud, Phoenix). Adaptoid T2 already expects operational observability — align LLM traces with that tier, not T0 toys.

---

## 5. Eval / benchmarks

### Public benchmarks (use correctly)

| Benchmark | What it measures | Production relevance | Official |
|---|---|---|---|
| **SWE-bench** (Verified / Lite / Full / Multilingual / Multimodal) | Real GitHub issue → PR resolve rate | Coding-agent capability; leaderboard ≠ product quality | [swebench.com](https://www.swebench.com/) |
| **Terminal-Bench** (harbor-native) | Agent mastery of terminal environments | CLI/harness agents (closest to coding OS loops) | [tbench.ai](https://www.tbench.ai/) |
| **GAIA** | General assistant tasks (tools, web, multi-step) | Tool-using assistant ceiling | [HF gaia-benchmark](https://huggingface.co/gaia-benchmark) |
| **Domain benches** (security, RAG, voice, …) | Narrow skill | Only if product is that domain | various |
| **Custom golden tasks** | *Your* acceptance criteria | **Highest product relevance** | project `evals/` |

### Elite eval stack (what to encode)

1. **Golden task suite** (human-written, versioned, no bench contamination) — mandatory for agent-product archetype.
2. **Graders:** code assertions > schema checks > LLM-as-judge (calibrated) > human sample.
3. **pass@k / pass^k** and seed stability (matches research-ml archetype thinking).
4. **Offline CI eval** on PR (small, fast) + **online** sampling in prod (Langfuse/LangSmith/Phoenix experiments).
5. **Cost/step/time budgets** as first-class metrics (SWE-bench culture already plots cost vs resolve).
6. **Canaries** in public-bench data; never train or few-shot on test.

### Encode vs never hardcode

| Encode | Never hardcode |
|---|---|
| `evals/` layout, grader interface, ship-check hook | “Must hit X% SWE-bench” as release gate for unrelated products |
| Offline golden path in CI | Running full SWE-bench in every PR |
| Online eval sampling rate + alert thresholds | Public leaderboard rank as marketing-only success |
| Separate **deterministic CI** vs **nondeterministic agent eval** | Replacing unit tests with LLM judges |

---

## 6. MCP ecosystem patterns (allowlist & security)

### Official risk surface (MCP Security Best Practices)

From [modelcontextprotocol.io security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices):

| Attack / anti-pattern | Required direction |
|---|---|
| **Confused deputy** (OAuth proxy + static client_id + consent cookie) | Per-client consent **before** third-party auth; exact `redirect_uri`; secure state |
| **Token passthrough** | **MUST NOT** accept tokens not issued to the MCP server |
| **SSRF** via OAuth metadata URLs | HTTPS; block private/link-local IPs; egress proxy; careful redirects |
| **Session hijacking** | Sessions ≠ auth; bind session to user; secure random IDs |
| **Local server compromise** | Treat local MCP as high privilege; least tool surface |

### Patterns elite hosts encode

1. **Deny by default** — tool invoke only if on **explicit allowlist** (name + version + schema).
2. **Server allowlist** — only approved MCP server identities/endpoints; fail closed.
3. **Least privilege scopes** — no `*` / omnibus OAuth scopes; separate read/write.
4. **Human-in-the-loop** for high blast-radius tools (deploy, payments, shell, prod DB).
5. **Schema validation** on all tool args (JSON Schema / Zod / Pydantic).
6. **Audit log** every tool call with principal, server, args hash, outcome.
7. **Network policy** for remote MCP: no metadata endpoints, no RFC1918.
8. **Skills vs MCP** — procedural knowledge (skills) is not the same as execution authority (MCP tools).

### Encode vs never hardcode

| Encode in harness / policies | Never hardcode |
|---|---|
| Allowlist structure in `policies/*.yaml` | Marketplace “install all” |
| FM-20 style: MCP write/network = high blast-radius | Trust any `npx` MCP from chat |
| Default MCP for Core scaffolds: `filesystem`, `git` (already engine) | Random SaaS MCPs in every archetype |
| Consent + OAuth resource-server rules when exposing remote MCP | Token passthrough “for simplicity” |

**Railway example:** platform documents CLI + local MCP + remote OAuth MCP + skills — harness should teach *when* each is appropriate, not wire remote deploy MCP by default.

---

## 7. GitHub Actions + agent CI patterns

### Two layers (do not conflate)

| Layer | Nature | Use for |
|---|---|---|
| **Deterministic CI** | Reproducible YAML: install, lint, type, unit, integration, `ship-check` | Merge gates, release |
| **Agentic / Continuous AI** | Nondeterministic agent loop in Actions (review, triage, propose patches) | Assistive automation with guardrails |

Official CI baseline: [GitHub Actions continuous integration](https://docs.github.com/en/actions/get-started/continuous-integration) — build/test on events; PR status checks.

### Elite agent-CI patterns (2026)

1. **Keep ship-check deterministic** — agents never replace unit/integration as sole gate.
2. **Scoped permissions** — `contents: read` default; write only on labeled workflows; protect `main`.
3. **Sandbox agent jobs** — no prod secrets; optional sparse checkout; network allowlist.
4. **Explicit instruction loading** — avoid unbounded auto-discovery of all `.github/**` skills (token overflow risk in mature repos); prefer **explicit** instruction inputs for review bots.
5. **Two runtimes:**
   - Full agent loop (Copilot agentic workflows / similar) for multi-step code work.
   - Single-turn LLM action (comment/review) for cheap PR triage.
6. **Human merge** — agent may open PR; human or required reviews merge.
7. **Eval workflow** — scheduled or path-filtered golden evals with cost caps; artifacts for traces.
8. **No silent force-push / secret exfil** — deny tools that print env; mask secrets.

### Encode vs never hardcode

| Encode | Never hardcode |
|---|---|
| CI matrix: types → lint → unit → (integration) → validators | Specific third-party Action SHA without pin policy |
| Optional `eval.yml` with timeout + budget env | Agentic workflow as required merge check for all repos |
| Branch protection assumptions | GitHub-only (keep hooks for GitLab later as interface) |
| Artifact upload for agent logs/traces | Unlimited `GITHUB_TOKEN` write |

---

## 8. Cross-cutting “default stack hint” vocabulary (proposed for Core)

Capability tags suitable for `stack_hints` / archetype tables (vendor-neutral):

```
runtime:     edge_http | edge_durable | vm_long | worker_queue | cli_local
api:         fastapi | nextjs | node_http | none
data:        postgres | sqlite | none
vector:      none | pgvector | dedicated_vector
cache:       none | redis_protocol
observe:     otel | none
eval:        golden | golden+online | none
mcp:         filesystem,git | (+allowlisted...)
deploy_hint: vercel | cloudflare | fly | railway | render | compose | undecided
```

**Rules:**

- `deploy_hint` is **soft** (documentation + optional templates), not a hard dependency install.
- `observe: otel` default from T2 / agent-product upward.
- `vector` only when brief mentions memory/RAG/search.
- `mcp` grows only via allowlist policy, never free-form scrape.

---

## 9. Adopt / watch / refuse (for Adaptoid product)

### Adopt (encode as hints / docs / policies)

- Postgres-first + pgvector-before-dedicated-vector.
- OTEL-shaped agent tracing; optional Langfuse/LangSmith/Phoenix backends.
- Golden evals + deterministic CI separation.
- MCP deny-by-default, no token passthrough, SSRF/private-IP blocks (align `policies/` + FM-20).
- Runtime class selection over vendor selection in engine tables.
- Railway/CF-style “agent skills for platform ops” as **optional** high-blast skills packs.

### Watch

- Cloudflare Agents SDK maturation as durable runtime standard.
- GitHub agentic workflows vs explicit single-turn agent Actions.
- AI SDK HarnessAgent (wrap Claude Code/Codex-style harnesses in product apps).
- Harbor / Terminal-Bench as harness-regression suite (optional Core plugin, not required).

### Refuse

- Scaffolding every project with full SaaS stack (Vercel+Supabase+Pinecone+LangSmith+…).
- Public bench scores as product definition of done.
- Unallowlisted remote MCP with deploy/prod credentials.
- Replacing ship-check with LLM-only evaluation.

---

## 10. Evidence gaps (next waves)

- [ ] Deep-read Vercel AI SDK HarnessAgent + policy tool approvals vs Adaptoid blast-radius.
- [ ] Neon branching × agent preview envs pattern.
- [ ] Qdrant/Pinecone multi-tenant agent memory reference architectures (official only).
- [ ] Full MCP authorization spec pass (OAuth resource server) for remote tool products.
- [ ] Terminal-Bench harbor integration feasibility for Adaptoid validators (optional).
- [ ] Enterprise APM (Datadog LLM Obs) mapping to OTEL fields we already want.

---

## Sources (primary)

See also `docs/research/era-ocean/sources/INDEX.md` (this wave’s entries).

1. https://ai-sdk.dev/docs/agents/overview  
2. https://developers.cloudflare.com/agents/  
3. https://docs.railway.com/agents  
4. https://fly.io/  
5. https://render.com/docs/postgresql  
6. https://langfuse.com/docs  
7. https://docs.langchain.com/langsmith  
8. https://arize.com/docs/phoenix  
9. https://docs.helicone.ai/  
10. https://www.swebench.com/  
11. https://www.tbench.ai/  
12. https://huggingface.co/gaia-benchmark  
13. https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices  
14. https://docs.github.com/en/actions/get-started/continuous-integration  
15. Adaptoid internal: `adaptor/engine.py` (`pull_ecosystem`), `tiers/TIERS.md`, `protocols/verification.md`
