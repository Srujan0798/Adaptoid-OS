# FM-20 — MCP / tool trust & injection

**Symptom.** Agent follows malicious tool descriptions, installs unvetted MCP servers, or treats MCP I/O as sandboxed when it is not. Data exfil or silent prod writes.

**Root cause.** MCP and marketplace plugins treated as trusted; Codex-class hosts may sandbox **shell** but not **MCP**; no allowlist.

**Prevention.**
- Allowlist MCP in `adaptoid.config.yaml` + OAP policy.
- Prefer CLI (`git`, `gh`, tests) over MCP when possible.
- Network/write MCP = blast-radius ≥ r3 (human confirm).
- Never auto-install marketplace plugins in generated projects.
- Treat tool descriptions as untrusted unless server is pinned and known.

**Detection.** `oap_security.sh` / policy pack; unexpected MCP servers in config; hooks PreToolUse deny where available.

**Recovery.** Revoke server, rotate secrets, audit session events, pin versions.
