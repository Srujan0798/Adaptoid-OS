# Adaptor — Input Taxonomy

> Load during the ANALYZE step. Archetypes (`archetypes/`) classify the *project*; this taxonomy classifies the *request*. The two are orthogonal: "fix hallucination in my bot" inside a SaaS project is archetype `saas-product` × input type `PROBLEM`. The input type picks the workflow shape; the archetype picks the adaptation profile.

## The 15 canonical input types

| Type | Signal phrases | Workflow shape | Mandatory output |
|---|---|---|---|
| PROJECT | build, create, develop, launch | plan → decompose → execute → verify → deliver | design doc + milestones + working artifact |
| PROBLEM | fix, solve, broken, not working | symptom → hypotheses → diagnose → fix → verify | root-cause analysis + fix + rollback plan |
| RESEARCH | analyze, study, survey, state of | scope → sources → extract → synthesize → cite | report with ≥2 independent sources per claim |
| TASK | write a script/function/query | extract requirement → generate → light verify | working artifact + usage note |
| JOB | prepare for, interview, study for | gap analysis → curriculum → practice → assess | learning plan + practice material |
| HACKATHON | 24/48/72 hours, ship fast | ruthless scope → prototype → demo polish → pitch | hour-by-hour plan + demoable MVP |
| STARTUP | validate idea, MVP, pitch | deconstruct → market scan → MVP spec → validation plan | lean canvas + MVP spec + experiment design |
| IDEA | what if, concept, imagine | capture → feasibility → recommend | pursue / pivot / park with rationale |
| LEARNING | teach me, explain, how does X work | assess level → scaffold → deliver → check | explanation at right level + practice |
| ANALYSIS | compare, vs, trade-off, which | criteria → evidence → matrix → recommend | comparison matrix + recommendation + sensitivity |
| CREATION | write a post/article/script | audience → outline → draft → refine | finished artifact + audience brief |
| DEBUG | why is it failing, stack trace | capture → reproduce → isolate → fix → prevent | minimal repro + fix + prevention note |
| OPTIMIZE | faster, cheaper, improve, scale | baseline → bottleneck → fix → re-measure | before/after metrics + trade-offs |
| MIGRATE | move from X to Y, upgrade, port | inventory → target → gap → pilot → migrate → validate | migration plan + rollback procedure |
| AUDIT | is this secure/compliant, review | scope → standard → evidence → gaps → roadmap | findings with severity + remediation order |

Detection: keyword match (signals above) + structure. If two types score within a small margin, ask — `protocols/clarification-protocol.md` — never guess silently.

## Three modulating axes

After type detection, three axes scale the response:

**Duration** — QUICK (<1 h) · SHORT (1 d–1 wk) · MEDIUM (1 wk–3 mo) · LONG (>3 mo) · EVENT (24–72 h).
Maps to tier sizing in `tiers/TIERS.md`.

**Complexity** — SIMPLE (familiar, clear) · MODERATE (some unknowns) · COMPLEX (novel domain, tight constraints) · CHAOTIC (ambiguous/conflicting — run clarification first).

**Risk** — LOW (personal, reversible) · MEDIUM (team, some stakes) · HIGH (production, customer-facing) · CRITICAL (money, safety, compliance).
Maps to blast-radius gates and verification depth.

## Verification scaling matrix (risk × complexity)

| | LOW | MEDIUM | HIGH | CRITICAL |
|---|---|---|---|---|
| **SIMPLE** | minimal | light | standard | full |
| **MODERATE** | light | standard | full | maximum |
| **COMPLEX** | standard | full | maximum | maximum + audit |
| **CHAOTIC** | full | maximum | maximum + audit | HITL required |

- minimal = runs, no syntax errors · light = lint + manual check · standard = lint + tests + review
- full = standard + security scan + integration tests · maximum = full + compliance + perf + staging
- maximum + audit = maximum + immutable audit trail + multi-party review

(The concrete gates live in `protocols/verification.md`; this matrix only decides *how many* slices of cheese.)

## Dynamic scaling during execution

| Condition | Trigger |
|---|---|
| time remaining <20% and scope incomplete | cut nice-to-haves; verification drops to smoke-test on cut items only — never on shipped ones |
| quality below bar and time available >30% | add a refactor/verify pass |
| new requirements appear mid-run | hold in backlog; finish current scope first (FM-08) |
| blocked >30 min on one issue | try fallback route; escalate to human if fallback fails |

## Integration map

| Concern | File |
|---|---|
| Project-type adaptation profile | `archetypes/<detected>.md` |
| Size/tier decision | `tiers/TIERS.md` |
| Ambiguous input | `protocols/clarification-protocol.md` |
| Typed intent output | `templates/root/PROJECT-INTENT.md` |
| Engine transform | `adaptor/ADAPTOR_ENGINE.md` (ANALYZE step) |
| Domain playbooks per type | `reference/workflows/` |
