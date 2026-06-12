# Hacker News Launch Post

**Title:** Show HN: Adaptoid OS — an agent operating system with 18 failure modes and validators

**Body:**

Most agentic AI projects fail for the same 18 reasons: state drift, false "done" claims, context bloat, route tampering, silent config reverts, etc. Frameworks give you primitives; they don't give you an operating system that catches these failures.

I built Adaptoid OS as a framework-agnostic harness that sits above LangGraph/CrewAI/AutoGen and adds:

- Typed PROJECT-INTENT.md → typed execution DAG
- 18 documented failure modes (FM-01 → FM-18) with executable validators
- Deterministic safety layer: Route Sentinel, VaultMMU, OAP
- Living-folder memory, event sourcing, audit chains
- v5.0 protocol layer for self-monitoring, memory-identity, evolution, proactive assistance, and workflow patterns

Everything is validated by `bash validators/dogfood.sh` before it ships.

Repo: https://github.com/Srujan0798/Adaptoid-OS

Looking for feedback on the failure-mode library and the validator-first approach.
