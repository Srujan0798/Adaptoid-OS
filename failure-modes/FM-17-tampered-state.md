# FM-17 — Tampered State / Undetected Context Drift

**Symptom.** A file's contents change silently between reads. The agent makes decisions on stale or corrupted state. An attacker or bug modifies `HANDOFF.md`, `EXECUTION.md`, or memory files without detection.

**Root cause.** No cryptographic integrity check on durable state files. Filesystem trust model assumes only the agent writes, which is false in multi-process or multi-user environments.

**Blast.** Wrong decisions, replay attacks, undetected sabotage, compliance violations.

**Prevention rule.**
- Every write to `orchestrator/memory/` computes a SHA-256 hash.
- Hashes are stored in `.vault/hashes.json` as a hash chain.
- Every read recomputes and verifies the hash.
- Mismatch = `STATE_TAMPERED` event + halt.

**Validator.** `validators/vault_mmu.sh`:
- Recomputes SHA-256 of tracked memory files.
- Verifies chain continuity against `.vault/hashes.json`.

**Wire-in.** `vault_mmu.sh` runs before every merge and before session resume.

**Fix when it fires.** Investigate the tampered file, restore from git or last known-good hash, regenerate if needed.
