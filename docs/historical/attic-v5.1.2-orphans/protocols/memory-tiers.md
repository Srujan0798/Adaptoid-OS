# Memory Tiers Protocol

A reference architecture for organizing agent memory into four latency-optimized tiers. This is an engineering pattern for long-running agents, not a theory of mind or identity. Memory persistence improves continuity across sessions; it does not imply sentience, consciousness, or selfhood.

---

## Overview

Long-running agents need more than a single context window. A tiered design separates hot session state from durable knowledge, experiences, and learned procedures. Each tier uses a backend matched to its access pattern and retention requirements.

```
User / Agent Interaction
         |
         v
+----------------------+
| L1: Working Memory   |  Hot, session-scoped state
+----------------------+
         |
         | logging / retrieval
         v
+----------------------+
| L2: Episodic Memory  |  Experiences and interaction history
+----------------------+
         |
         | consolidation
         v
+----------------------+
| L3: Semantic Memory  |  Facts, entities, relationships
+----------------------+
         |
         | skill extraction
         v
+----------------------+
| L4: Procedural Memory|  Skills, workflows, behavioral rules
+----------------------+
```

---

## L1: Working Memory

**Role:** Active session context — the contents the agent keeps immediately available.

**Suggested contents:**

| Block | Purpose |
|---|---|
| Agent persona block | Core role, values, communication style. |
| User context block | Key facts about the current user and task. |
| Emotional / stance tracker | Detected mood, sentiment trends, weighted associations. |
| Session context | Recent messages (sliding window), active tool outputs, in-flight operations. |

**Backend suggestions:**

| Component | Suggestion | Rationale |
|---|---|---|
| Primary | In-process context window | Fastest access; no network round-trip. |
| Hot-state failover | Redis OSS | Sub-millisecond hot state across micro-restarts. |

**Latency target:** < 1 ms for reads.

**Lifecycle:** Session TTL. Cleared or archived when the session ends.

**Default size:** ~100 MB or context-window equivalent; configurable.

---

## L2: Episodic Memory

**Role:** A diary of what happened, when, and with what result. Preserves nuance that flat facts lose.

**Suggested contents:**

- Interaction logs with timestamps
- Decision chains and reasoning traces
- Outcome records (success, failure, user feedback)
- Temporal index
- Compressed episode summaries
- Sentiment and importance scores

**Backend suggestions:**

| Component | Suggestion | Rationale |
|---|---|---|
| Semantic search | Qdrant or similar vector DB | Fast similarity search over episodes. |
| Temporal indexing | TimescaleDB or other time-series DB | Range queries and event ordering. |

**Latency target:** ~20 ms p99 for vector search.

**Lifecycle:** Permanent storage with decay-based pruning. High-importance episodes fade slowly; routine interactions fade faster.

**Episode schema (example):**

```json
{
  "timestamp": "2026-07-01T14:12:00Z",
  "type": "interaction",
  "content": "User asked for a vegetarian restaurant recommendation.",
  "entities": ["user", "diet", "restaurant"],
  "sentiment": 0.6,
  "importance_score": 0.4,
  "source_session": "sess_abc123"
}
```

---

## L3: Semantic Memory

**Role:** Timeless facts, learned concepts, and entity relationships. Structured so the agent can answer relational and temporal questions.

**Suggested contents:**

- Entity graph (people, projects, concepts)
- Fact store with confidence and provenance
- Preference profiles
- Bi-temporal edges (`valid_from`, `valid_to`, `invalid_at`)
- Confidence scores and access statistics

**Backend suggestions:**

| Component | Suggestion | Rationale |
|---|---|---|
| Knowledge graph | Neo4j + Graphiti | Temporal knowledge graph with bi-temporal edges. |
| Semantic surface | Qdrant | Vector index for fuzzy matching before graph traversal. |

**Latency target:** 20–50 ms p99 for hybrid queries.

**Lifecycle:** Permanent, with explicit invalidation and versioning. Old facts are marked superseded rather than overwritten.

**Fact schema (example):**

```json
{
  "fact": "User prefers vegetarian meals",
  "confidence": 0.95,
  "source_episode_ids": ["ep_2847", "ep_3012"],
  "valid_from": "2026-01-15T09:23:00Z",
  "valid_to": null,
  "invalid_at": null,
  "access_count": 47,
  "last_accessed": "2026-07-01T14:12:00Z",
  "emotional_weight": 0.3
}
```

---

## L4: Procedural Memory

**Role:** The "how" layer — skills, workflows, behavioral rules, and self-knowledge. Curated and version-controlled rather than automatically grown.

**Suggested contents:**

- `PERSONA.md` — core identity, values, behavioral principles
- `SKILLS.md` — learned capabilities and workflow templates
- `SELF_KNOWLEDGE.md` — capability registry and known limitations
- `USER_PROFILES/` — per-user adaptation rules
- `WORKFLOWS/` — executable workflow definitions
- `TOOLS/` — function-calling schemas

**Backend suggestions:**

| Component | Suggestion | Rationale |
|---|---|---|
| Storage | Git-tracked markdown | Human-readable, versioned, supports rollback. |
| Loading | Parse at startup | Inject into context at session start. |

**Latency target:** < 100 ms at startup to load and parse.

**Lifecycle:** Permanent, version-controlled. Sensitive changes (persona, values) should require human approval.

**Example layout:**

```
$L4_MEMORY/
├── PERSONA.md
├── SKILLS.md
├── SELF_KNOWLEDGE.md
├── USER_PROFILES/
│   ├── alice.md
│   └── bob.md
├── WORKFLOWS/
│   ├── onboarding.yaml
│   ├── data_analysis.yaml
│   └── escalation.yaml
└── TOOLS/
    └── function_schemas/
```

---

## Tier Comparison

| Tier | Name | Backend | Latency | Contents | Lifecycle |
|---|---|---|---|---|---|
| L1 | Working | In-process + Redis OSS | < 1 ms | Session state, persona, user context | Session TTL |
| L2 | Episodic | Qdrant + time-series DB | ~20 ms p99 | Experiences, transcripts, outcomes | Permanent, decay-pruned |
| L3 | Semantic | Neo4j + Graphiti + Qdrant | 20–50 ms | Facts, entities, relationships | Permanent, bi-temporal |
| L4 | Procedural | Git-tracked markdown | N/A (load at startup) | Skills, workflows, self-knowledge | Version-controlled |

---

## Data Flow

```
User Interaction
       |
       v
+------------------+    Tool Calls      +------------------+
|   L1: Working    | <---------------> |   Agent LLM      |
|   Memory         |                   |                  |
+--------+---------+                   +------------------+
         |
         | session logging
         v
+------------------+    Consolidation   +------------------+
|   L2: Episodic   | -----------------> |   L3: Semantic   |
|   Memory         |   (dream cycle)    |   Memory         |
+--------+---------+                    +--------+---------+
         |                                       |
         | pattern extraction                    | skill extraction
         v                                       v
+------------------+                     +------------------+
|   Cold Storage   |                     |   L4: Procedural |
|   (pruned mems)  |                     |   Memory         |
+------------------+                     +------------------+
```

---

## Configuration Example

```yaml
memory:
  tiers:
    l1_working:
      backend: redis
      host: localhost
      port: 6379
      default_size_mb: 100
      ttl_seconds: 3600

    l2_episodic:
      vector_backend: qdrant
      qdrant_url: http://localhost:6333
      temporal_backend: timescaledb
      database_url: postgres://localhost/timescale
      default_retention_days: 90
      fade_mem:
        enabled: true
        sml_half_life_days: 30
        lml_half_life_days: 365

    l3_semantic:
      graph_backend: neo4j
      neo4j_uri: bolt://localhost:7687
      graphiti_enabled: true
      bi_temporal: true

    l4_procedural:
      storage: git
      repo_path: /var/adaptoid/l4_memory
      auto_commit: true
      require_approval_for:
        - PERSONA.md
        - core_values
```

---

## Operational Notes

- **Do not treat memory as identity.** Persistent memory improves continuity and personalization; it does not create consciousness, sentience, or a self.
- **Namespace per user.** Prevent cross-user contamination at the storage layer.
- **Version L4 changes.** Rollback is critical when a learned skill degrades behavior.
- **Monitor poisoning.** See the consolidation-cycle protocol for the security scan step.
- **Start simple.** A 4-tier system can be overkill for short-lived agents; adopt tiers incrementally based on session length and continuity requirements.
