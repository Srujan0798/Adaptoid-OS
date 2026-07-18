# Audit — closed final (v5.3.0)

**Date:** 2026-07-18 · **Status:** READY TO USE (+ era adapt)

## Product surfaces (authoritative)

| Surface | Path | Verdict |
|---|---|---|
| **Lite** | **`ADAPTOID-LITE.md`** (repo root; Desktop copy ok) | Only standalone product |
| **Core** | **This whole folder** + `adaptor/engine.py` | Default for real projects |
| Legacy | `reference/OS_SETUP_v1.3_full.md` | Stub redirect only |
| Attic | `docs/historical/` | Do not load for normal use |

## Multi-agent corner audit (summary)

- Core generate path works with skills + ship docs; hollow pro removed
- Lite brand unified; entry graph closed
- Live 2026 adopted: skills, worktrees, host matrix, agent-product, FM-19/20
- Leftovers (SDLC acceptance hardness, macOS hash, PreToolUse templates): `ADAPTATION.md`

## Flow

```
USE / START_HERE
  Lite → paste ADAPTOID-LITE.md + brief → adapt & complete
  Core → engine --host all → project with SHIP-SYSTEM + .agents/skills
       → host runs SDLC × playbook → preflight → done with evidence
```

## Gate

```bash
make ship-check
```

PASS required before claiming product ready. Evidence: command output.
