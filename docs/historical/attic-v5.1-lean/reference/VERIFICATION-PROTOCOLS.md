# 🛡️ VERIFICATION-PROTOCOLS.md

> *How Adaptoid-OS makes hallucinations and wrong routes **expensive to commit**
> and **cheap to detect**. Mandatory bootstrap reading. This is the second most
> important file in Adaptoid-OS — read it after ADAPTOID-ENGINE.md.*

---

## 0. The thesis

> **A wrong answer that has been verified is a learning event.
> A wrong answer that has not been verified is a silent failure.**

Verification in Adaptoid-OS is **not a final step**. It is a *layered, in-line
discipline* that runs at four levels:

1. **At the schema layer** — every output is a typed object (Pydantic AI / BAML
   / Zod), so the *shape* of the answer is checked before its *content*.
2. **At the evidence layer** — every claim in the answer is bound to a source
   the Adaptoid can re-fetch and re-check.
3. **At the route layer** — every non-read action is matched against the
   *Intent* of the project, the *Type* of the target, and the *State* of the
   system, before it runs.
4. **At the cross-check layer** — for high-stakes decisions, an *independent
   second pass* (different model family, different tools, or human) confirms
   the first.

These four layers, composed, are what makes Adaptoid's verification regime
*defensible* — and what makes the Adaptoid contract (§7 in
`ADAPTOID-ENGINE.md`) enforceable.

---

## 1. The four-layer model (visual)

```
                         ┌─────────────────────────────────┐
                         │  Cross-check layer              │
                         │  (different model / human)      │
                         │  ▲                               │
                         │  │  high-stakes only             │
                         ├─────────────────────────────────┤
                         │  Route layer                    │
                         │  (intent ↔ type ↔ state)        │
                         ├─────────────────────────────────┤
                         │  Evidence layer                 │
                         │  (claim → source)               │
                         ├─────────────────────────────────┤
                         │  Schema layer                   │
                         │  (Pydantic AI / BAML / Zod)     │
                         └─────────────────────────────────┘
                              ▲                ▲
                              │                │
                       every output       every output
                       (always)         (always)
```

A failure at any layer **fails the node** and triggers rollback per
`ADAPTOID-ENGINE.md` §3.2.

---

## 2. Layer 1 — Schema (the cheapest, most powerful layer)

### 2.1 The principle

If the output cannot be parsed as the type the consumer expects, **it is wrong
by definition** — regardless of how fluent the text looks.

### 2.2 The toolchain

| Tool                                                | Best for                                                     | Notes                                                        |
| --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Pydantic AI** (≥ 1.0)                             | Python, type-safe agents, MCP-friendly                        | The default for Adaptoid's reference runtime                  |
| **BAML**                                            | Multi-language, structured-output LLM calls, schema-as-tests  | Use when the project ships TS / Go / Rust alongside Python    |
| **Instructor**                                      | Drop-in structured outputs for any OpenAI-compatible API    | Lightest, great for one-offs                                  |
| **Outlines**                                        | Constrained generation (regex / JSON-schema / CFG)           | Use when you need *guaranteed* format (e.g. tool calls)      |
| **Zod** (TS) / **JSON Schema** + codegen            | TypeScript / Node side                                       | Mirror the Python types, do not drift                        |

### 2.3 The Adaptoid pattern

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class CodeClaim(BaseModel):
    claim: str
    evidence: list[str]              # ← every claim is bound to evidence
    confidence: float = Field(ge=0, le=1)
    route_safe: bool                  # ←  passed route-check?

agent = Agent(
    model="openai:gpt-4o",
    result_type=CodeClaim,
    system_prompt="...",              #  from PROJECT-INTENT.md binding
)
```

If the model returns text that cannot be parsed into `CodeClaim`, **the node
fails**. There is no "soft parsing" path. (Pydantic's `validation_error` becomes
the diagnostic and the Adaptoid retries with a corrective prompt, but never
silently coerces.)

### 2.4 The anti-patterns Adaptoid forbids

- ❌ `agent.run(prompt).data` without a `result_type`
- ❌ "Best effort" JSON parsing
- ❌ String-matching the output
- ❌ Trusting the model's *self-reported* confidence
- ❌ Letting the LLM invent field names

---

## 3. Layer 2 — Evidence (every claim, every time)

### 3.1 The principle

A model that can be re-prompted can lie. A model that must cite a source it can
be re-fetched from can be **checked**.

### 3.2 The evidence-first output schema

Every claim in every Adaptoid output follows:

```yaml
claims:
  - text: "POST /v1/charges accepts `amount` in cents"
    evidence:
      - type: "url"           # or "file", "git_commit", "mcp_call", "code_symbol"
        ref: "https://stripe.com/docs/api/charges/create"
        retrieved_at: "2026-06-09T19:50:00Z"
        verbatim: "amount: integer, required — Amount in cents"
  - text: "..."
    evidence: [...]
unsupported:                   # ← explicit, never silently dropped
  - "The exact rate-limit headers vary by endpoint and are not in scope"
```

### 3.3 The Evidence Enforcer (pseudocode)

```python
def enforce_evidence(out, ctx):
    for claim in out.claims:
        if not claim.evidence:
            return Verification.fail("missing evidence", node=out.id)
        for ev in claim.evidence:
            if not can_re_fetch(ev, ctx):
                return Verification.fail("stale evidence", node=out.id)
            actual = re_fetch(ev, ctx)
            if not supports(actual, claim.text):
                return Verification.fail("evidence contradicts claim", node=out.id)
    return Verification.ok()
```

`can_re_fetch` understands:
- URLs (HTTP HEAD + content-hash; archives in `memory-bank/evidence/`)
- Files in repo (path + git-commit + content-hash)
- MCP tool calls (replay; record in `memory-bank/mcp-transcript.jsonl`)
- Code symbols (resolve symbol; read source)

### 3.4 MCP as the *default* evidence substrate

The Adaptoid-OS stack ships with a curated set of MCP servers
(`config/mcp/*.json`). For any claim about a *system* the Adaptoid has access
to, the **default evidence is an MCP call**, not a URL scrape. This is the
single biggest lever against "I made up an API" hallucinations, and it is the
reason the Adaptoid stack is MCP-first.

### 3.5 Where evidence is *not* required

Some outputs are not claims — they are artefacts. The protocol still requires
*structured* output, but the evidence requirement applies to *interpretive*
content, not to e.g. "the test file has 47 lines." The line is drawn by
`non_negotiables` in `PROJECT-INTENT.md` and by node-level `guards`.

---

## 4. Layer 3 — Route (the anti-wrong-route layer)

### 4.1 The principle

A wrong route is **doing the right thing in the wrong place**. The fix is
*binding every action to a route-check* that compares:

- **Intent** — what the project is *for* (from `PROJECT-INTENT.md`).
- **Type** — what the target *is* (its schema, its file extension, its kind).
- **State** — what the world *is right now* (memory-bank, git status, env).

If any of the three are inconsistent with the proposed action, **the action is
rejected**, with a corrective prompt that names the inconsistency.

### 4.2 The RouteCheck contract

```python
class RouteCheck(BaseModel):
    action: str                       # e.g. "rm -rf adaptoid/.cache"
    target: str                       # e.g. "adaptoid/.cache"
    intent_match: bool                # is this action on the path to SC-* ?
    type_match: bool                  # is the target the right *kind* of object ?
    state_match: bool                 # is the world in the state we expect ?
    reasoning: str                    # ≤ 200 chars, no fluff
    safe_to_proceed: bool
```

The route-check is **always run before any non-read side-effect** — and
optionally before reads on cold paths.

### 4.3 Worked example: the "right tool, wrong file" anti-pattern

Suppose the project intent says "fix the failing test in `tests/test_pricing.py`"
but the agent proposes to *edit* `src/payments/stripe.py`. The RouteCheck sees:

- `intent_match`: false (the goal is "fix test", not "edit source first")
- `type_match`: false (Stripe source is unrelated to the failing test)
- `state_match`: ? (irrelevant, fails earlier)

→ **Reject** with: "Your action edits `src/payments/stripe.py`, but `PROJECT-INTENT.md`
SC-1 is about `tests/test_pricing.py`. Re-read the failing test's assertion
before proposing a source edit."

This is the *opposite* of letting the agent "try it and see." The cost of
saying no here is 2 seconds. The cost of letting it ship a wrong-route edit is
hours.

### 4.4 The dangerous-but-allowed pattern: pre-image rollback

Some actions are *legitimately* destructive but necessary (drop a database,
reset a sandbox, force-push a branch). The protocol requires that the action
be:

- **Marked `destructive: true`** in the node definition.
- **Bounded by a `RollbackSpec`** with a real `pre_image_required: true` (the
  controller will refuse to run without one).
- **Wrapped in a `durable` step** when the action is irreversible (Temporal /
  Inngest / DBOS will refuse to run it as a non-durable step).

This is the "make it reversible, or don't do it" rule.

---

## 5. Layer 4 — Cross-check (for high-stakes decisions)

### 5.1 The principle

Some decisions are too important for a single verifier. Examples:

- Production deploys
- Schema migrations
- Security-relevant refactors
- Anything that touches `data_sensitivity: regulated` data
- Any claim whose `confidence < 0.5` after the first three layers

For these, the controller schedules a **second independent pass**:

- A different model family (e.g. `claude-3-5-sonnet` ↔ `gpt-4o`)
- A different toolchain (Pydantic AI ↔ BAML)
- A different lens (a "red team" node, a human)

### 5.2 The cross-check contract

```yaml
cross_check:
  policy: "always|on-low-confidence|on-destructive|on-regulated"
  when: { confidence_lt: 0.6 }
  pass:
    - agent: "red-team"
      prompt: "Find a way this output is wrong. Cite the source you would check."
    - human: { role: reviewer, channel: "slack:#adaptoid-alerts" }
  reconcile: "first-dissent-halts"     # if red-team and human disagree, halt
```

### 5.3 Calibration probes

The Adaptoid ships a `calibration/` set: a small (~50-case) labeled corpus per
domain. Before the controller trusts its own self-reported confidence, it
runs the probe and **calibrates** the confidence scale to the historical
agreement rate. This is the layer that defends against "the model is 99%
confident and 60% right."

---

## 6. The verification runtime (what ships)

Adaptoid-OS ships with a runnable verification layer at `scripts/verify.sh` and
a CI-friendly `scripts/verify-ci.sh`. They are wired by default to run on:

- Every pull request (`verify-ci.sh`)
- Every Skill version bump (`verify-skills.sh`)
- Every change to `PROJECT-INTENT.md` (`verify-intent.sh`)

The runtime uses `Promptfoo` for LLM-as-judge evals, `DeepEval` for metric
assertions, and the `calibration/` set as a holdout. The OTel traces of every
verification step are shipped to the configured observability backend.

---

## 7. The "wrong-route" taxonomy (full list)

The following is the canonical list of wrong-route anti-patterns Adaptoid's
RouteCheck recognizes. Each maps to a specific guard. See
`adapters/problem-adapter.md` for the full control mapping.

| Anti-pattern ID | Description                                            | Control |
| --------------- | ------------------------------------------------------ | ------- |
| `WR-1`          | Right tool, wrong file                                  | RouteCheck + `target ∈ goal-path` |
| `WR-2`          | Right API, wrong version                                | Pinned versions; `MCP-versions` in evidence |
| `WR-3`          | Right user intent, wrong user                           | Identity check on multi-tenant ops |
| `WR-4`          | Right semantic action, wrong sequence (out-of-order)   | DAG preconditions enforced |
| `WR-5`          | Right test, wrong branch                                | RouteCheck on `git_branch` vs. `intent` |
| `WR-6`          | Right env, wrong account                                | `account_id` in evidence |
| `WR-7`          | Right command, wrong scope (path / namespace / DB)     | `--dry-run` first; RouteCheck on scope |
| `WR-8`          | Right model, wrong context (cache / stale tool result) | `cache-control: no-cache` on cold paths |
| `WR-9`          | Right skill, wrong domain (e.g. medical advice for code) | Skill `domain` tag matched against intent `domain` |
| `WR-10`         | Right intent, wrong commit / branch (edits on main)    | RouteCheck on `git_branch` policy |
| `WR-11`         | Right action, wrong auth scope (token can't do it)      | Pre-flight auth check on every privileged op |
| `WR-12`         | Right message, wrong recipient (PII to wrong team)      | Redaction + recipient ACL |

---

## 8. The "hallucination" taxonomy (full list)

| Anti-pattern ID | Description                                            | Control |
| --------------- | ------------------------------------------------------ | ------- |
| `H-1`           | Fabricated API / endpoint                               | MCP-first + evidence-required |
| `H-2`           | Fabricated citation                                    | Re-fetch + content-hash |
| `H-3`           | Fabricated commit / file path                          | Git pre-image + path existence check |
| `H-4`           | Fabricated version number                              | Pin to a known registry / changelog |
| `H-5`           | Fabricated person / quote                              | Source binding; refuse to proceed if no source |
| `H-6`           | Fabricated numeric result ("3.2x speedup")              | Reproduce in `reports/eval-*` |
| `H-7`           | Fabricated function signature                          | Type-check via Pydantic / BAML on the actual code |
| `H-8`           | "I checked" when it didn't                             | MCP-call transcript is the source of truth |
| `H-9`           | "Per the docs" when docs don't say that                | Verbatim quote required in evidence |
| `H-10`          | Plausible-but-wrong defaults                           | Pydantic default audit on every output |
| `H-11`          | Time-fabrication ("last commit was 3 days ago")        | Re-query git log; refuse if > freshness window |
| `H-12`          | Library hallucination (importing a non-existent module) | Import-resolution check before claim of "works" |

---

## 9. CI integration (the rules that are *enforced*, not "suggested")

`.adaptoid/ci/` ships with:

- `verify-intent.sh` — fails the build on schema-invalid `PROJECT-INTENT.md`
- `verify-skills.sh` — fails on stale or untested skills
- `verify-citations.sh` — fails on any unsourced claim in `reports/`
- `verify-costs.sh` — fails on any node whose `cost_cap_usd` exceeds profile
- `verify-dag.sh` — fails on any plan with a cycle, missing rollback, or
  undeclared preimage
- `verify-evals.sh` — fails on any regression in the calibration set
- `verify-redteam.sh` — runs the red-team probe against the latest plan and
  fails on a successful exploit

These run on PRs by default. Skip only with a human-authored `// adaptoid:
allow-verify-skip reason="..."` annotation, which is itself logged.

---

## 10. The "falsification" mindset

Every plan emitted by the Adaptoid includes a `falsification` block:

```yaml
falsification:
  - "If the eval set is < 50 cases, this plan is not valid"
  - "If ollama is not running on the dev box, plan must be downgraded"
  - "If the user has not signed off on SC-2 within 24h, plan halts"
```

This is the *opposite* of "trust the model." It is **structural skepticism**:
the Adaptoid is required to enumerate, in advance, the conditions under which
its own plan is not valid, and the controller halts on any of them.

---

## 11. TL;DR

> Adaptoid's verification is **four layers, all always-on, all
> checkable-by-anyone**. Schema first (the cheapest), evidence second (the
> deepest), route third (the most contextual), cross-check fourth (the
> strongest). Combined with a falsification mindset and a CI that *enforces*
> rather than *suggests*, the cost of a hallucination or a wrong route is
> high to commit and low to detect. That is the entire point.

🜂
