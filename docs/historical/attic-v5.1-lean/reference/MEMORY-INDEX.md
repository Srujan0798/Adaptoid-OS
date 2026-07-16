# 🗄️ MEMORY-INDEX.md

> *The living, queryable memory protocol. How the Adaptoid remembers setup,
> decisions, facts, and lessons — across sessions, across agents, across weeks.*

---

## 0. The thesis

> An Adaptoid's memory is **durable, structured, queryable, and source-bound**.
> It is not a chat log. It is not a vector store you have to remember to read.
> It is **a folder of Markdown files + a generated SQLite index + a graph of
> cross-references** that every agent in the system is *required* to consult at
> session-start and *required* to write to at every checkpoint.

The cost of this discipline is ~5 seconds per session-start and ~30 seconds per
checkpoint. The benefit is the **permanent elimination of "we forgot the setup"**
as a class of failure.

---

## 1. The memory model (three layers)

```
                          ┌──────────────────────────────────────────┐
                          │  Layer 3 — Procedural memory             │
                          │  (Skills: skills/*/SKILL.md)             │
                          │  "How to do X"                            │
                          └──────────────┬───────────────────────────┘
                                         │  references
                          ┌──────────────▼───────────────────────────┐
                          │  Layer 2 — Episodic + Semantic memory     │
                          │  (memory-bank/facts/, decisions/, ADR/)  │
                          │  "What we know / decided / learned"      │
                          └──────────────┬───────────────────────────┘
                                         │  references
                          ┌──────────────▼───────────────────────────┐
                          │  Layer 1 — Working memory (in-context)    │
                          │  (the plan, the active node, the ctx)     │
                          │  "What we are doing right now"           │
                          └──────────────────────────────────────────┘
```

- **Layer 1** lives in the controller's runtime (not on disk).
- **Layer 2** is the durable, queryable, version-controlled memory bank.
- **Layer 3** is the procedural memory — the skills library — and is
  versioned and tested independently.

A useful rule of thumb: **if you would need to ask the user twice, it belongs
in Layer 2.**

---

## 2. The `memory-bank/` directory

The default location is `adaptoid/memory-bank/` (the bootstrap script creates
it). The structure:

```
memory-bank/
├── INDEX.md                     # ←  this file, mirrored here for cold-start
├── index.sqlite                 #   generated; FTS5 over the bank
├── facts/                       #   "X is true" — with sources
│   ├── 2026-06-09-stripe-charges-amount-cents.md
│   ├── 2026-06-09-our-postgres-major-version.md
│   └── …
├── decisions/                   #   "We chose X over Y" — ADRs
│   ├── ADR-0001-use-pydantic-ai.md
│   ├── ADR-0002-llm-routing-policy.md
│   └── …
├── sessions/                    #   Per-session transcripts (summarized)
│   ├── 2026-06-09-session-001.md
│   └── …
├── lessons/                     #   "This failed, here's why"
│   ├── L-001-ollama-cold-start-slow.md
│   └── …
├── mcp-transcript.jsonl         #   append-only log of every MCP call
├── evidence/                    #   cached evidence (URL content, etc.)
│   └── …
└── snapshots/                   #   point-in-time digests (weekly auto)
    └── 2026-W23.md
```

Every file in this tree is **plain Markdown with YAML frontmatter** so it is:

- Diff-able in git
- Readable by any agent cold-start
- Indexable by `scripts/memory-sync.sh` (which builds the SQLite FTS index)

### 2.1 The frontmatter contract (mandatory)

```yaml
---
id: F-2026-06-09-stripe-charges-amount-cents   # unique, stable
kind: fact                                       # fact | decision | lesson | session | evidence
created: 2026-06-09T19:50:00Z
updated: 2026-06-09T19:50:00Z
ttl: P90D                                         # how long this remains load-bearing
sources:
  - type: url
    ref: https://stripe.com/docs/api/charges/create
    retrieved_at: 2026-06-09T19:50:00Z
    content_hash: sha256:abc…
confidence: 0.95
supersedes: []                                    # previous fact IDs this replaces
superseded_by: null
tags: [stripe, payments, api, "data-amount"]
related: []                                      # cross-links to decisions/lessons
falsification: "If Stripe docs change, this fact is invalid"
---
```

### 2.2 The TTL discipline

Every fact has a `ttl`. On session-start, the controller:

1. Indexes the bank.
2. Flags any fact whose `created + ttl < now`.
3. For each flagged fact, either re-verifies it (preferred) or moves it to
   `memory-bank/lessons/` with `kind: stale-fact` and `superseded_by: null`.
4. Surfaces the re-verification work in the plan.

This is the discipline that prevents the "we used a 2-year-old fact as
load-bearing" failure mode.

---

## 3. The cold-start contract (the *first* read after PROJECT-INTENT)

Order:

1. `MEMORY-INDEX.md` (this file)
2. `memory-bank/INDEX.md` (mirror, for redundancy)
3. `memory-bank/index.sqlite` — open the FTS index
4. Run `memory-search.sh "<top 3 active SC-IDs>"` — get the top relevant
   facts/decisions/lessons
5. Cross-reference with the `PROJECT-INTENT.md`'s `known_failure_modes` and
   load the lessons for each
6. *Then* read skills/ and the rest of the system

This takes ~5 seconds and is non-negotiable. The session-start hook enforces it
for Claude Code (`config/claude-code/hooks/session-start.sh`); the runtime
enforces it for any other harness.

---

## 4. The memory search contract

Agents do **not** free-form read the memory bank. They call a typed search
function:

```python
class MemoryQuery(BaseModel):
    intent: list[str]                              # SC-IDs, topics
    kinds: list[Literal["fact","decision","lesson","session","evidence"]]
    max_age: str | None = "P7D"                    # ISO duration
    min_confidence: float = 0.6
    require_sources: bool = True
    exclude_superseded: bool = True
    limit: int = 25

class MemoryHit(BaseModel):
    id: str
    kind: str
    title: str
    snippet: str
    score: float
    sources: list[str]
    age: str                                        # human-readable
    confidence: float

class MemorySearch(BaseModel):
    query: MemoryQuery
    hits: list[MemoryHit]
    empty: bool                                     # true if no hits — investigate
    reason: str                                     # if empty, why (e.g. "all stale")
```

The **typed return** is the key. The agent cannot, for example, confabulate
"a fact from 2 months ago" because the schema requires `age` and
`min_confidence` to be reported.

### 4.1 When search returns empty

This is itself a signal. The protocol:

- If `empty: true` and `reason: "all stale"`, the controller schedules
  re-verification work.
- If `empty: true` and `reason: "no matches"`, the agent is required to
  *acknowledge the gap* before proceeding.
- If `empty: true` for a `fact` with high `severity` in `known_failure_modes`,
  the controller halts and asks the human.

---

## 5. The write contract (the *only* way to add to the bank)

Agents do **not** free-form write. They call a typed writer:

```python
class MemoryWriteRequest(BaseModel):
    kind: Literal["fact","decision","lesson","session","evidence"]
    body_md: str
    sources: list[Source]                           # required for facts
    confidence: float = Field(ge=0, le=1)
    ttl: str | None = None                          # ISO duration; required for facts
    supersedes: list[str] = []
    tags: list[str] = []
    related: list[str] = []
    falsification: str | None = None
```

The controller:

1. Validates the schema.
2. Generates a stable `id` (kind + ISO date + slug).
3. Rejects any fact without a `source` (or moves it to `lessons/` with
   `kind: unverified`).
4. Updates the SQLite index.
5. Cross-references `supersedes` / `superseded_by`.
6. Logs the write to `mcp-transcript.jsonl`-equivalent for memory itself.

### 5.1 The "lessons" writer (the most important writer)

Lessons are the failure-mode memory. Every time something goes wrong — a
hallucination caught, a wrong route blocked, a calibration probe failing — the
controller writes a `lessons/` entry. The discipline:

```yaml
---
id: L-2026-06-09-ollama-cold-start-slow
kind: lesson
created: 2026-06-09T19:50:00Z
ttl: P365D
trigger: "First LLM call on a fresh Ollama container took 47s"
root_cause: "Model not yet in ollama's mmap cache; first-token-latency dominates"
fix: "Pre-warm the model at bootstrap with a single tiny completion"
prevention: "scripts/bootstrap.sh now runs ollama warmup if local_runtime: ollama"
tags: [ollama, perf, cold-start]
related: [F-2026-06-09-our-llm-primary-is-ollama]
falsification: "If we move off Ollama, this lesson is invalid"
---
```

The next session's `MemoryQuery("performance issues", kinds=["lesson"])` will
return this, and the Adaptoid will not pay the cold-start tax again.

---

## 6. Cross-agent memory (the A2A / multi-agent layer)

When the Adaptoid runs multiple agents, they all share the same `memory-bank/`
on the same filesystem. A2A (Google) and MCP (Anthropic) both define ways to
expose this over a network; Adaptoid ships:

- A local `mcp-memory-server` (read/write/search the bank over MCP).
- An A2A-compatible `adaptoid-memory-agent` for cross-process multi-agent
  setups.

This means **memory is not per-agent, not per-session, not per-host** — it is
**per-project**, with a defined ACL in `memory-bank/.acl.yaml`.

### 6.1 The ACL (default)

```yaml
# memory-bank/.acl.yaml
default: read
write:
  - kind: fact
    min_confidence: 0.7
    require_sources: true
    allowed_agents: ["*"]                 # anyone can write a *sourced* fact
  - kind: lesson
    allowed_agents: ["controller", "red-team", "reviewer"]
  - kind: decision
    require_adr_template: true
    allowed_agents: ["controller", "owner"]  # only owner-role can write ADRs
  - kind: session
    allowed_agents: ["*"]
redact:
  - field: sources[*].ref
    match: "*.example.com"
    strategy: "hash"                       # privacy-preserving, still dedupable
```

---

## 7. The graph (cross-references are first-class)

`memory-bank/` is a **directed graph**:

- `fact` ↔ `fact` (via `supersedes` / `superseded_by`)
- `fact` ↔ `decision` (via `related`)
- `decision` ↔ `lesson` (via `related`)
- `lesson` ↔ `known_failure_mode` (via `tags` / `related`)
- `evidence` ↔ `fact` (via `sources`)

`scripts/memory-graph.py` renders this as a DOT file; `scripts/memory-viz`
launches a local web viewer. The graph is a forcing function for *consistency*
— if a `lesson` exists but no `decision` references it, that's a gap.

---

## 8. Backup, retention, and disaster recovery

- **Backup**: the `memory-bank/` is git-versioned by default. A weekly
  snapshot is also written to `snapshots/`. For regulated workloads, the
  bootstrap can wire it to S3 / GCS / Azure Blob.
- **Retention**: facts default to `ttl: P90D`, decisions to `ttl: P365D`,
  lessons to `ttl: P365D` (or `P∞D` for canonical lessons). TTL is *advisory*;
  the controller prompts re-verification, never silently deletes.
- **Disaster recovery**: `scripts/memory-restore.sh` re-hydrates the SQLite
  index from Markdown. Loss of `index.sqlite` is non-fatal.

---

## 9. Privacy, secrets, and the redaction layer

The memory layer is **the single most privacy-sensitive component** of an
Adaptoid deployment. The protocol requires:

- **All writes pass through the redaction layer** (`scripts/redact.py`). The
  redaction patterns are configurable per `data_sensitivity`.
- **Secrets are never written to facts**. If a fact *requires* a secret to
  reproduce, the secret is referenced by hash, not value.
- **URL evidence is fetched through a content-hash cache** so a single
  retrieval serves many claims.

---

## 10. The "memory you can take with you"

Because `memory-bank/` is plain Markdown + a generated index, you can:

- Zip it and hand it to a colleague.
- Grep it on the command line.
- Render it to a static site (`scripts/memory-viz --export`).
- Migrate it to any other Adaptoid-compatible system.

This is the point. Memory is **portable, inspectable, durable** — never
trapped inside a vendor's database.

---

## 11. TL;DR

> Adaptoid's memory is a plain-Markdown folder with a typed frontmatter
> contract, a generated SQLite FTS index, a graph of cross-references, a TTL
> discipline, and an ACL. Every agent reads it at session-start, writes to
> it at every checkpoint, and searches it through a typed contract. The
> 5-second discipline is the price of never forgetting the setup again.

🜂
