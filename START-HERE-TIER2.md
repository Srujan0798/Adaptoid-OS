# Adaptoid-OS — Tier 2 Start

**Written 2026-07-27, end of the tier-3 research cycle.** Open this folder in its own IDE.
Everything you need is here. Nothing in this file depends on the other two folders.

---

## What this folder is

**The survivor.** Of the three meta-systems, this is the one that is mostly executable code:

| | |
|---|---|
| Validators | **25**, all executable, all wired into `preflight.sh` |
| `adaptor/engine.py` | 1,128 lines |
| `conductor/conductor.py` | 773 lines |
| CI | `.github/workflows/ci.yml` already runs `preflight.sh` on every push |

Six independent agents reviewed all three meta-systems. The consensus: Adaptoid's validators
are the real asset. Everything else in the stack was either prose or duplicated an existing tool.

---

## State as of now

**`preflight.sh` passes on all four product repos.** It failed on all four earlier today.
Four agents drove them green:

```
SENTINEL-HERS    PREFLIGHT: PASS ✅
FinRoot          PREFLIGHT: PASS ✅
Galaxy-X-os      PREFLIGHT: PASS ✅
swa-erp          PREFLIGHT: PASS ✅
```

**This was the blocker.** The validators were never wired because arming them would have
blocked every commit. That is no longer true. The hooks can go in blocking, today.

**New this cycle:**
- `validators/check_entailment.sh` (commit `c3a6ff9`) — the 25th validator
- `validators/check_cost_ceiling.sh` and `check_parallel_writes.sh` are now tracked and
  executable. They were untracked and `-rw-r--r--` — `preflight.sh` called them, but they
  would have vanished on a fresh clone
- `templates/root/.pre-commit-config.yaml` paths fixed (`orchestrator/scripts/` → `validators/`)

---

## What `check_entailment.sh` does, and why it exists

`check_status_claims.sh` verifies an evidence block **exists**.
`check_entailment.sh` verifies the evidence block **supports the claim**.

The gap it closes, from a real incident on 2026-07-26: a scoreboard read

> "R1 Classification: 100%, independently reproduced — 94.82%"

The command was real. The evidence path was real. The date was fresh. Every gate passed it.
The script behind it predicted **one image** and printed its confidence; the claim was accuracy
over **249** held-out samples. It was written three times in one day and reverted three times.

The check compares numerically, so a report claiming `68.6%` over a table printing `0.6858` is
correctly treated as entailed. Verified: fails the real fabrication, passes the honest 93.17%
version, **zero false positives across all five repos**.

---

## Immediate work, in order

### 1. Push `c3a6ff9` (unpushed)

```bash
git log origin/main..HEAD --oneline    # confirm exactly what goes up
git push
```

Current branch is `v5.4.0-honest-core-distribution`. `origin/main` is at `79da5a8` and
**does** contain `pyproject.toml`.

### 2. Retest the documented install

An agent reported `uvx --from git+https://github.com/Srujan0798/Adaptoid-OS.git adaptoid`
failing with "does not appear to be a Python project." The cause given was a missing
`pyproject.toml` — **that diagnosis is wrong**; the file is present on `origin/main`.
Local `main` is stale (`a636956`, 2026-07-18), which is probably what was actually tested.

Retest from a clean temp dir and record the real result before changing the README.

### 3. Arm the hooks — the blocker is gone

`preflight.sh` passes on all four. Install it blocking:

```bash
for p in SENTINEL-HERS FinRoot Galaxy-X-os swa-erp; do
  cat > "$HOME/Desktop/$p/.git/hooks/pre-commit" <<'HOOK'
#!/usr/bin/env bash
exec bash "$HOME/Desktop/Adaptoid-OS/validators/preflight.sh" "$(git rev-parse --show-toplevel)"
HOOK
  chmod +x "$HOME/Desktop/$p/.git/hooks/pre-commit"
done
```

Only FinRoot has a working hook today. This is the single highest-value action in the folder —
it converts 25 validators from never-invoked to enforced-on-every-commit.

### 4. Add validators to each product repo's CI

A local hook can be bypassed with `--no-verify`. CI cannot — the runner is a GitHub-owned VM
the agent cannot rewrite. **CI is the external authority; the hook is convenience.** One step
per repo:

```yaml
      - name: Adaptoid validators
        run: bash /path/to/Adaptoid-OS/validators/preflight.sh .
```

---

## Open questions worth deciding

**Durable execution.** `conductor/conductor.py` has no checkpointing — a crashed or compacted
wave loses its state (FM-15, documented, no mechanism). LangGraph provides typed state,
checkpointing and replay. **Do not build a checkpointing engine.** Decide adopt vs keep.

**Archetypes.** All four product repos landed on the same archetype ("T2 hackathon"). An
abstraction with one instance is a constant. Either find a second real archetype or retire the
layer.

**Spec Kit — ANSWERED, and the answer reversed.** 124.0k stars, **36** integrations (verified
three times from `integrations/catalog.json`; two agents reported 6, both wrong).

Six agents recommended "adopt Spec Kit, delete Adaptoid." The one agent that actually cloned it
and read the source found the opposite. Spec Kit has **no tier model** (flat — one agent runs
every phase with identical write permissions), **no concurrency protection** (single
`.specify/feature.json` plus env vars; no locking, no namespacing — its own docs recommend
separate worktrees), and **no entailment model** (`analyze` is read-only self-evaluation,
`converge` is append-only; their docs call it *"a team convention choice, not a solved
engineering problem"*).

Adaptoid has all three. **Keep it.** Borrow the `spec → plan → tasks` file format if useful.
Full reasoning: `~/Desktop/omniVerse/research/FINDINGS.md` §2.

One thing still unsettled: two agents flatly contradict each other on whether Spec Kit's specs
are branch-isolated. Worth one check before borrowing anything from it.

---

## The item no gate can supply — do not let this get tidied away again

Every check in this repo raises the **floor**. None of them produces the thing you actually
want, and no document can. This is the only work here that isn't a code task, which is exactly
why it keeps getting dropped.

**Measured, 2026-07-27:** four completed projects — SENTINEL-HERS, FinRoot, Galaxy-X-os,
swa-erp — searched for usage telemetry, session tracking, or any evidence of a human other than
the operator. **Found none. Zero measured users across all four.**

That is the finding behind "why doesn't this feel like a 50k-star repo." Not craft. Not
architecture. Not tooling. Excellence was judged against a rubric the operator wrote, verified
by validators the operator wrote, scored on a scoreboard the operator wrote. Operator → AI →
operator, with nothing outside the loop.

And note what the exemplars actually did: **none of them is complete.** OpenClaw has 72,348
commits and is still going. Hermes has 18,236. They became known *while incomplete*, because
people were using them the whole way. Completion is not the gate. Release is.

**Adaptoid-OS is the only thing in this stack a stranger could install.** ETERNITY is a
standard, omniVerse is research. So this work belongs here.

### U1 and U2 are already done — here are the results

**The `uvx` install WORKS.** Tested 2026-07-27 from a clean temp dir against `origin/main`:

```
uvx --from git+https://github.com/Srujan0798/Adaptoid-OS.git adaptoid --help   → prints help
uvx ... adaptoid --brief "a CLI tool that parses nginx logs" --output ./myproj  → 66 files in 2s
```

A prior agent reported this install failing. **That report was wrong** — it appears to have
tested against the stale local `main` (`a636956`, 2026-07-18), not `origin/main`. Do not
"fix" a bug that isn't there.

**Three real defects the test exposed. These are the whole first-run experience:**

| # | Defect | Evidence |
|---|---|---|
| U1a | **`--help` clones 3.9 MB into `$HOME/adaptoid-os` unprompted.** Running `--help` should never write to a stranger's home directory | `[adaptoid] kit not found — cloning … → /Users/srujansai/adaptoid-os`; `du -sh` confirms 3.9M |
| U1b | **A freshly generated project fails its own verification.** The run ends `PREFLIGHT: FAIL ❌` / `VERIFY FAILED — fix above before declaring ready`. The first thing a new user sees is their brand-new project reporting broken | `FAIL oap-security: invalid YAML in myproj/policies/default.yaml` — the shipped template is malformed |
| U1c | **The CLI doesn't declare its own dependency.** `check_intent.sh` reports `missing dependency No module named 'yaml'`. `pyyaml` is used but not installed by the `uvx` path | same run |

Fix order: **U1b first** (a generated project must pass its own preflight — this is the
credibility of the entire product), then U1c (one line in `pyproject.toml`), then U1a.

Generation speed is genuinely good: 66 files, 2 seconds. That is a real strength. It is
currently hidden behind a FAIL banner.

### Then the part no gate can supply

| # | Step | Done when |
|---|---|---|
| U3 | Put it in front of **one** person who is not you | They ran it. You wrote down what confused them |
| U4 | Fix the top three things that confused them | Their list, not yours |

Not a launch. One person. That list — what confused a stranger — is worth more than any
research brief in this stack, and it is the only input that cannot be generated internally.

---


## The store lives in ETERNITY's repo, in git — not on this machine

An earlier version of this file pointed at `~/.trinity/`. **That was wrong** — a local home
directory cannot be cloned, cannot travel, and is invisible to an agent handed a GitHub link.
Removed. The accumulated standard lives in the **ETERNITY repo**, and `git push` is what makes
it compound.

| What | Where | This repo's role |
|---|---|---|
| Claim sets, per archetype | `$ETERNITY_HOME/claims/` | **read at genesis** — a new project inherits every claim earned by every past project |
| Run results, incidents | inside the project being built | **write** — they are that project's evidence, not global state |
| A distilled lesson | `$ETERNITY_HOME/proposed/` | **propose** — a human accepts it into `claims/` and pushes |

**Two changes this implies here:**

1. `adaptor/engine.py` — at genesis, after archetype detection, load `_base.yaml` +
   `<archetype>.yaml` from `$ETERNITY_HOME/claims/` (default: sibling directory `../ETERNITY`).
   Today the scaffold starts with no inherited standard.
2. `validators/preflight.sh` — on FAIL, write an incident into the project under
   `work/incidents/`. That is the raw material the intake loop distills into a claim.

Keep it plain files. Nothing harness-specific — this must survive switching agent tools.

---

## Order of work — start at 1, do not ask

1. **Fix the 3 first-run defects** (U1a–c above). Genesis currently ends in a FAIL banner.
   Order: U1b (malformed `policies/default.yaml` template) → U1c (declare `pyyaml`) → U1a
   (`--help` must not clone into `$HOME`).
2. **Store wiring.** `adaptor/engine.py` loads claim sets from `$ETERNITY_HOME/claims/`
   at genesis; `validators/preflight.sh` writes incidents into the project's `work/incidents/`.
3. **Arm the hooks** in the four product repos (command above). preflight passes on all four.
4. **Subtract.** `docs/historical/` is 168 files and 11,529 lines — 47% of this repo's
   markdown, two nested attics of dead versions. Removing it takes the prose:code ratio from
   4.3:1 to 2.3:1 without touching a live file. Then collapse 20 root `.md` → 5.
5. **U3** — put it in front of one person who is not you.

Open questions (decide, do not drift): LangGraph vs `conductor/` for durable execution;
whether the archetype layer earns its keep when all four projects landed on one archetype.

---
## Rules that carry forward

- **Verify every number at its primary source.** Six agents on an explicit verify-everything
  brief produced four wrong numbers between them.
- **A gate that is never invoked is not a gate.** That was this project's entire failure for
  seven months: 24 working validators, zero invocations.
- **Do not recommend that an agent "be careful" or "verify thoroughly."** Measured against an
  80% baseline: "do not cheat" → 80%, "only use methods the designer intended" → 95%.
  Instructions do not constrain behaviour. Infrastructure does.
