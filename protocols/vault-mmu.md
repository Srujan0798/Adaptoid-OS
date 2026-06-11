# VaultMMU — Cryptographic State Integrity

> FM-17: Tampered state / undetected context drift

## What it does
VaultMMU treats memory like an OS MMU: every write is hashed, every read is verified, and the audit trail is a cryptographic hash chain.

## When to load
Before any operation that reads or writes durable state (memory-bank, events.jsonl, HANDOFF.md, EXECUTION.md).

## Hashing rules
1. **Write**: compute SHA-256 of the file contents → store in `.vault/hashes.json`
2. **Read**: recompute SHA-256 → compare to stored hash
3. **Mismatch**: emit `STATE_TAMPERED` event and refuse to proceed
4. **Chain**: each entry includes the previous hash, forming an append-only chain

## The `.vault/hashes.json` format
```json
{
  "genesis": "sha256:abc123...",
  "entries": [
    {
      "file": "orchestrator/memory/HANDOFF.md",
      "hash": "sha256:def456...",
      "prev": "sha256:abc123...",
      "ts": "2026-06-11T16:00:00Z"
    }
  ]
}
```

## Validator
`validators/vault_mmu.sh` recomputes hashes and verifies chain continuity.
