# Protocol — Sandboxing

> Load before running untrusted or agent-generated code, or when standing up the local harness. Code execution is the highest-risk surface in any agentic system. The rule: the agent that writes code never decides the blast radius of running it — the sandbox does.

## Isolation levels (pick the weakest that contains the risk)

| Level | Technology | Cold start | Isolation | Use for |
|---|---|---|---|---|
| 1 — Process | V8 isolates (e.g. Cloudflare Workers-style) | <1 ms | process-level, JS/WASM only | quick transforms, validation snippets |
| 2 — OS namespace | bubblewrap (Linux), Seatbelt (macOS) | ~10–50 ms | namespaces + seccomp | CLI tools: git, npm, build steps |
| 3 — Userspace kernel | gVisor (Docker `runsc`) | ~100 ms | syscall interception | untrusted Python/Node, package installs, scraping |
| 4 — MicroVM | Firecracker (e.g. E2B), Kata | ~90–150 ms | hardware VM boundary | full environments, long runs, anything touching prod-like data |

Selection rules:
- Agent-generated code you didn't review → **Level 3 minimum**.
- Network access required → any level, but **through a proxy with a domain allowlist**, never raw sockets.
- Long-running (>1 h) or GPU work → Level 4.
- Plain `docker run` without gVisor/Firecracker is a packaging tool, **not** a security boundary for hostile code.

## The four guarantees every sandbox must give

1. **Filesystem**: read/write only inside a designated ephemeral working directory. Paths outside are invisible. Directory destroyed on session end — no state leakage.
2. **Network**: deny by default. When needed, route through a host-side proxy enforcing a domain allowlist. DNS resolves on the host, not in the sandbox.
3. **Credentials**: secrets **never enter the sandbox**. The host holds tokens; sandboxed code makes requests via IPC/proxy and the host injects auth. Even a fully compromised sandbox cannot exfiltrate keys it never saw. Pass *references* (`secret:stripe_key`), not values.
4. **Resources**: hard caps on CPU time, memory, disk, file descriptors, processes (cgroups / VM limits). Fork bombs and runaway loops are contained, not debugged.

## Credential proxy pattern

```
+-------------+      +---------------+      +------------------+
|  Sandbox    | IPC  |  Unix domain  |      |  Secret store    |
|  (no keys)  +----->+  socket proxy +----->+  (host-only,     |
|             |      |  (allowlist)  |      |   no network)    |
+-------------+      +---------------+      +------------------+
```

- Env passed to sandbox contains references only: `STRIPE_KEY=secret:stripe_prod_key`.
- The proxy resolves references, injects headers, and logs every request (→ `policy.denied` / audit events).
- Socket permissions `0600`, owned by the host agent process.

## Hardening checklist (Linux namespace / container levels)

- [ ] All namespaces enabled (user, PID, mount, network, IPC, UTS)
- [ ] seccomp default-deny whitelist
- [ ] `/proc`, `/sys` read-only minimal subset
- [ ] tmpfs working dir with size limit
- [ ] non-root UID mapping inside the sandbox
- [ ] `CAP_DROP=ALL`, `no-new-privileges`
- [ ] never bind-mount `/var/run/docker.sock` into any sandbox
- [ ] sandbox cannot read the orchestrator's memory files or `adaptoid.config.yaml` secrets
- [ ] escape attempts logged to the event stream (`policy.denied`) and session killed

## Integration map

| Concern | Protocol / tool |
|---|---|
| Should this tool call run at all? | `protocols/oap-security.md` — policy check happens **outside** the sandbox, before it |
| Touches remote / money / humans? | `protocols/blast-radius.md` — sandbox level is part of the blast-radius decision |
| Unauthorized tool / destructive action | `failure-modes/FM-18-unauthorized-tool.md` |
| Local harness wiring | `setup/AGENTIC_OS_PROFILE.md`, `setup/harness/docker-compose.yml` |
| Escape / denial forensics | `protocols/event-sourcing.md` (`policy.denied` events) |

## Why this matters (incident-grounded)

Documented production incidents — an agent deleting a production environment, another wiping a database in seconds — share one root cause: the permission system *could physically perform* the destructive action. Prompts are not guardrails. A sandbox that cannot reach prod, holds no credentials, and dies on session end is a guardrail.
