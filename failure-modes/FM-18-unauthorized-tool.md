# FM-18 — Unauthorized Tool Call / Destructive Action Without Approval

**Symptom.** A worker calls `Bash(rm -rf /)` or `Write` to a production config without approval. A tool accesses PII or exfiltrates data. The orchestrator trusts the worker's tool choice implicitly.

**Root cause.** No deterministic policy enforcement at the tool-call boundary. Permissions are implicit or documented but not enforced.

**Blast.** Data loss, security breaches, compliance violations, production outages.

**Prevention rule.**
- OAP (Open Agent Passport) policy packs define ALLOW / DENY / REQUIRE_APPROVAL for every tool pattern.
- Default pack is DENY — no tool call without explicit policy.
- Policy packs are YAML, human-reviewable, version-controlled.
- Every tool call is logged with policy decision to events.jsonl.

**Validator.** `validators/oap_security.sh`:
- Checks `policies/` directory for valid YAML packs.
- Validates every tool mentioned in `adaptoid.config.yaml` has a matching policy.
- Flags missing packs.

**Wire-in.** OAP check runs before every tool invocation in worker sessions.

**Fix when it fires.** Block the tool call, add the missing policy, require human approval for the action.
