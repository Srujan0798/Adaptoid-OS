# Protocol — Clarification (Ambiguity Handling)

> Load when a brief is vague, garbled, or under-specified. The rule: **never guess silently** (kernel law). A wrong guess at intent compounds into FM-08 scope creep and FM-16 wrong routes. This protocol turns "do it the best way" into a typed, confirmable intent — in at most one round of ≤4 questions (the adaptor's interviewer rule).

## When it triggers

Score the incoming brief. Activate clarification when the total exceeds 60, or when archetype detection confidence is low, or when fewer than 3 concrete constraints are present.

| Signal | Weight |
|---|---|
| No clear subject / deliverable ("make it better") | +15 |
| Missing action verb | +15 |
| Subjective terms without context ("best", "fast", "cheap") | +12 |
| No time constraint | +10 |
| No budget / resource ceiling | +8 |
| No scope boundary | +8 |
| No measurable success criteria | +10 |
| No acceptance criteria | +8 |
| Heavy typos / fragmented or contradictory phrasing | +10–15 |

| Score | Action |
|---|---|
| 0–20 | Clear — proceed to adaptor ANALYZE normally |
| 21–40 | Mostly clear — ask 1–2 targeted questions inline |
| 41–60 | Moderate — run Steps 1–2 below |
| 61–80 | High — run all 4 steps |
| 81–100 | Severe — all 4 steps + restate what you *think* they meant before anything else |

## The four steps

### Step 1 — Deconstruct
Extract what's recoverable into an intent skeleton; mark the rest UNKNOWN.

```yaml
intent_skeleton:
  what: "<task / deliverable, best guess>"
  why: UNKNOWN | "<goal>"
  constraints: UNKNOWN | [..]
  success_criteria: UNKNOWN | [..]
  inferred_archetype: <from archetypes/>
  confidence: 0.0–1.0
```

### Step 2 — Guided inquiry (≤4 questions, multiple-choice preferred)
Ask only for UNKNOWN fields, ranked by information value:

1. P0 — domain/subject: "What is this about?"
2. P1 — goal: "What outcome makes this a success?"
3. P2 — constraints: "Deadline? Budget? Hard must-nots?"
4. P3 — definition of done: "How will we know it's good enough?"

Proceed when ≥3 of the 5 skeleton fields are filled. Do NOT iterate more than 3 rounds — after 3, deliver the best recommendation with assumptions explicitly flagged.

### Step 3 — Apply an analytical frame (only if the problem is a *decision*, not a build)
| Clarified problem shape | Frame |
|---|---|
| "X or Y?" / compare options | Decision matrix (criteria × weights), then sensitivity check |
| "Is X a good idea?" | First-principles deconstruction + cost-benefit |
| "Why did X fail?" | Inversion ("how would we guarantee this failure?") + 5-whys |
| "How to improve X?" | Baseline → bottleneck → fix → re-measure (see eval-driven-dev) |
| Strategy / positioning | SWOT, kept to one screen |
| Long-term / irreversible | Second-order consequences pass before committing |

One frame, one screen. Frames structure the recommendation; they don't replace evidence.

### Step 4 — Confirm and hand off
Present the filled intent skeleton + recommendation with assumptions labeled. On confirmation, write `PROJECT-INTENT.md` (validated by `validators/check_intent.sh`) and hand off to `adaptor/engine.py`. The clarified intent — not the original garbled brief — is what enters the event log (`intent.parsed`).

## Anti-patterns

- **Interrogation.** More than 4 questions in a round means you're outsourcing analysis to the user. Deconstruct harder first.
- **Silent guessing.** Filling UNKNOWN fields without flagging them. Every assumption must be visible in the output.
- **Frame theater.** Running SWOT on "rename this function." Frames are for genuine decisions only.
- **Endless refinement.** 3 iterations max. Ship the best recommendation with flagged residual uncertainty.

## Integration map

| Concern | Protocol / tool |
|---|---|
| Intent capture format | `templates/root/PROJECT-INTENT.md` + `schemas/ProjectIntent.schema.json` |
| Archetype detection | `adaptor/ADAPTOR_ENGINE.md` (ANALYZE step) + `adaptor/INPUT-TAXONOMY.md` |
| Planning questions discipline | `patterns/six-enforced-questions.md` |
| Scope protection downstream | `failure-modes/FM-08-scope-creep.md` |
