# Audit — closed final (v5.2.1)

**Date:** 2026-07-18 · **Status:** READY TO USE

## Product surfaces (authoritative)

| Surface | Path | Verdict |
|---|---|---|
| **Lite** | **`ADAPTOID-LITE.md`** (repo root; Desktop copy ok) | Only standalone product |
| **Core** | **This whole folder** + `adaptor/engine.py` | Default for real projects |
| Legacy | `reference/OS_SETUP_v1.3_full.md` | Stub redirect only |
| Attic | `docs/historical/` | Do not load for normal use |

## Flow

```
USE / START_HERE
  Lite → paste ADAPTOID-LITE.md + brief → adapt & complete
  Core → engine --core-only --host all → project with SHIP-SYSTEM
       → host runs SDLC × playbook → preflight → done with evidence
```

## Gate

```bash
make ship-check
```

PASS required before claiming product ready. Evidence: command output.
