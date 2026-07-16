# Deep audit — Adaptoid OS (competitor lens)

**Date:** 2026-07-16 · **Version audited:** 5.1.5 → fixes in 5.1.6  
**Lens:** new competitor reviewing Lite + Core end-to-end.

---

## Product surfaces (correct)

| Surface | Reality | Verdict |
|---|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` only | Correct name; file body still has **legacy** mid-file structure (skills/, old protocols) → agents can drift |
| **Core** | Entire this folder | Correct; engine path works with `--sdlc` |

---

## Flow that works today

```
USE.md
  Lite → paste OS_SETUP_v1.3_full.md + brief
  Core → engine --core-only --host all --sdlc → project with SHIP-SYSTEM + 7 tasks
       → host agent executes SDLC × toolkit → preflight
```

**Evidence:** dogfood PASS; engine generates AGENTS/CLAUDE/SHIP-SYSTEM + 01-plan…07-maintain.

---

## What is good

1. Clear Lite vs Core naming (after 5.1.5 fix)  
2. `SHIP-SYSTEM.md` fuses GFG SDLC + host toolkit  
3. Engine + conductor + preflight form a real spine  
4. Lean live tree (~127 files); historical attic separated  
5. Dogfood enforces no root LITE.md, no claw_bridge/skills on live tree  

---

## Gaps / unused / inefficiency (found)

| # | Issue | Severity | Fix |
|---|---|---|---|
| 1 | **Lite body drift** — OS_SETUP mid-file still describes archived skills/, dispatch-protocol, old tree | High | Canonical override block at top of OS_SETUP |
| 2 | **`--sdlc` not default** — users forget; incomplete Core UX | High | Default `--sdlc` on |
| 3 | **Entry doc sprawl** — USE / START_HERE / PRODUCT / FLOW / INDEX / 00-INVOCATION overlap | Med | 00-INVOCATION → thin pointer to USE; START_HERE already thin |
| 4 | **MANIFEST stale** — still says “Pro product”, v5.1.2, no SHIP-SYSTEM | Med | Rewrite MANIFEST |
| 5 | **SELECTION.md claimed as engine input** but engine uses hardcoded stacks | Med | FLOW honesty + engine comment; keep file as human ref |
| 6 | **sdlc-agile.yaml** not loaded by code (docs only) | Low | Keep as machine mirror of SHIP-SYSTEM stages |
| 7 | **benchmarks/last_results.json** noise if tracked | Low | gitignore + delete |
| 8 | **install.sh** still mentions 00-INVOCATION as primary | Low | Point to USE.md + Lite path |
| 9 | **HOST-CAPABILITIES.md** is a stub pointer** | Low | Keep (one hop to SHIP-SYSTEM) |
| 10 | **tiers/TIERS.md** not read by engine** | Low | Engine has own signals; TIERS is human/Lite ref — keep |

---

## Missing for “perfect competitor product”

| Missing | Notes |
|---|---|
| Auto dogfood of Lite paste path | Can’t fully automate “paste into Claude”; manual |
| Real user project completion | Kit works; business value needs real brief |
| OS_SETUP full rewrite | Too large; override block is pragmatic fix |

---

## Corrections applied in 5.1.6

See CHANGELOG. Summary: default `--sdlc`, MANIFEST/USE/install alignment, Lite canonical block, gitignore last_results, 00-INVOCATION → USE.
