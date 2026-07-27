# TRINITY — Adaptoid-OS as Brahmā

**Added:** 2026-07-27 · **Status:** proposal, nothing here is implemented yet
**Full spec:** `~/Desktop/omniVerse/docs/specs/2026-07-27-brahma-adaptoid-spec.md`
**Written, not committed.** Review before staging.

---

## What changes

Adaptoid becomes the **creator face** of a three-system environment:

| Face | System | Function |
|---|---|---|
| Brahmā — creator | **Adaptoid-OS** | intent → archetype → tier → project exists; dispatch |
| Viṣṇu — preserver | ETERNITY | the standard: what "excellent" means |
| Śiva — dissolver | omniVerse | destroys false claims; owns all state |

**The one rule that changes everything:** Adaptoid no longer decides what is finished. It
reads the red-claim list and dispatches against it. **The backlog is generated, not authored.**

Adaptoid may never verify, score, declare done, or author status. Those move to Śiva.

---

## External validation

The head of Claude Code, describing the higher-leverage move in agentic coding:

> "The shift is from turn-by-turn prompting to system design. […] Now the higher-leverage
> move is building a small system that **finds work, hands it out, checks it, records what
> happened, and decides the next step**."

That is this architecture, named by someone who arrived at it independently:
finds work (red claims) → hands it out (Adaptoid dispatch) → checks it (omniVerse) →
records what happened (ledger) → decides the next step (red list feeds back).

Same source, on verification: *"give it real verification — let it actually test what it's
building as a user, not just run tests."* That is the `proof-of-life` pack.

---

## Measured state, 2026-07-27

| Property | Value |
|---|---|
| Files | 240 `.md`, 48 `.sh`, 15 `.py` |
| Executable validators in `validators/` | **25, all functional** |
| Validators wired to a git hook or CI in any of 4 projects | **0** |
| Failure modes documented (`FM-01`…`FM-15`) | 15 |
| Failure modes with a detector | **0** |
| Archetypes | 12 |
| Archetypes with an executable claim set | 0 |

**The problem is not quality. It is that the quality is opt-in, and the party choosing to
opt in is the party being judged.**

### Two live bugs found while measuring

`validators/check_cost_ceiling.sh` and `validators/check_parallel_writes.sh` are
**untracked — never committed**. They exist only on this machine and vanish on a fresh
clone. This is the same class as a project marking a wave SHIPPED while its module was
never committed: FM-07 and FM-01, live, inside the system that defines them.

---

## Work order

Tasks 1–4 are unblocked and can start immediately.

| # | Task | Why |
|---|---|---|
| **1** | **`validator.adaptoid` predicate — wrap all 25 scripts** | **Highest leverage in all of TRINITY.** One predicate turns 25 working-but-never-invoked scripts into every-commit enforcement. Zero scripts rewritten. |
| 2 | Detectors for FM-01…FM-15; add `detector:` front-matter to each `failure-modes/*.md` | A failure mode without a detector is a description, not a guardrail |
| 3 | Validator-coverage self-claim: every `validators/*.sh` referenced by ≥1 claim | An unreferenced validator is dead code pretending to be a gate — the current state |
| 4 | Stop authoring status; read the ledger instead | Closes FM-01, FM-09, FM-14 structurally |
| 5 | Amend `kernel/TWO-TIER.md` — orchestrator owns the **spine** (golden path, integration seams), workers own **breadth** | Nobody currently holds the whole product; this is the incoherence |
| 6 | Orchestrator holds live context across a wave; handoff files become recovery, not the primary channel | The #1 documented multi-agent failure is infinite handoff loops — "agents keep replanning because nobody owns the task" |
| 7 | Map `protocols/blast-radius.md` r0–r3 to real DevContainer isolation | Security research: prose controls provide zero protection; enforcement must sit at a boundary the agent's code cannot cross |
| 8 | Promote `check_cost_ceiling.sh` to a `metric.lte` claim | Cost stops being a script nobody runs |
| 9 | Bind each of the 12 archetypes to an ETERNITY claim set | Selecting an archetype selects an executable definition of done |
| 10 | Decide `conductor/` vs LangGraph on evidence | A crashed or compacted wave currently loses all state — FM-15 with no mechanism. **Do not build a checkpointing engine.** |

---

## Scope boundary

Adaptoid must not become a verifier (that recreates party-judges-itself), a standard
(that is Viṣṇu), a model router, or a memory system (the ledger is episodic memory already).

---

## Self-improvement, mechanically

1. **Every caught failure adds a detector.** `omni learn` proposes; adoption requires an
   explicit lock update. The FM list grows from evidence, never imagination.
2. **Archetype calibration from outcomes.** `calibration/` already has `generate_cases.py`
   and `cases.json`. If `hackathon-T2` projects consistently go red on the same claims, the
   archetype's claim set was wrong — not the projects.
3. **Assert validator coverage about Adaptoid itself.** The system that checks others must
   be checkable.
