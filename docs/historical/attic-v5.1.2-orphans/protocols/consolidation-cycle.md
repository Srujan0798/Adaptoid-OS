# Memory Consolidation Cycle Protocol

A background pipeline that converts short-term memory signals into durable, structured knowledge. The design borrows names from biological sleep cycles as a metaphor for batch maintenance operations: **Light Sleep**, **REM Sleep**, **Deep Sleep**, and **Prune**. This is an engineering pattern for long-running agents, not a model of consciousness.

---

## When it runs

The consolidation cycle should run during idle periods, at the end of a session, or on a scheduled basis. It must be non-blocking so that foreground agent operations are not delayed.

| Trigger | Use case |
|---|---|
| `on_idle` | Run when the agent has been inactive for a configured threshold. |
| `end_of_session` | Run immediately after a session terminates. |
| `scheduled` | Run at a fixed time (e.g., 02:00 local time) for predictable batch load. |

The cycle can also be triggered manually for debugging or recovery.

---

## Pipeline overview

```
+-----------------------------------------------------------+
|              MEMORY CONSOLIDATION PIPELINE                 |
+-----------------------------------------------------------+
|                                                           |
|  PHASE 1: LIGHT SLEEP  -> Ingest & deduplicate            |
|  PHASE 2: REM SLEEP    -> Reflect & extract patterns      |
|  PHASE 3: DEEP SLEEP   -> Score & promote                 |
|  PHASE 4: PRUNE        -> Forget & archive                |
|  PHASE 5: SECURITY SCAN -> Detect anomalies               |
|  PHASE 6: SELF-ASSESSMENT -> Summarize & propose updates  |
|                                                           |
+-----------------------------------------------------------+
```

---

## Phase 1: Light Sleep — Ingest & Deduplicate

**Purpose:** Collect new episodic entries and remove near-duplicates.

**Actions:**

1. Gather all L2 episodes created since the last cycle.
2. Deduplicate using a similarity threshold (e.g., Jaccard > 0.9 → merge).
3. Extract candidate facts and entities.
4. Compute an initial importance score using lightweight heuristics or an LLM signal.

**Outputs:**

- Deduplicated episode set
- Candidate facts and entities
- Initial importance scores

---

## Phase 2: REM Sleep — Reflect & Extract Patterns

**Purpose:** Find recurring themes and generate candidate insights.

**Actions:**

1. Cluster recent episodes by theme.
2. Identify patterns that appear across multiple episodes.
3. Cross-reference candidates with existing L3 knowledge.
4. Generate candidate insights for promotion.

**Outputs:**

- Pattern candidates
- Confirmed / contradicted facts
- Candidate insights for Deep Sleep scoring

---

## Phase 3: Deep Sleep — Score & Promote

**Purpose:** Decide which candidates deserve long-term retention and where they should live.

**Scoring weights (example):**

| Signal | Weight | Meaning |
|---|---|---|
| Relevance | 0.30 | Importance to recent conversations. |
| Frequency | 0.24 | How often the memory has been recalled. |
| Query diversity | 0.15 | Referenced from different task types. |
| Recency | 0.15 | Temporal freshness. |
| Cross-phase reinforcement | 0.10 | Supported by multiple consolidation passes. |
| Conceptual richness | 0.06 | Depth of connections to other memories. |

**Promotion thresholds (example):**

| Threshold | Value |
|---|---|
| Minimum score | 0.8 |
| Minimum recalls | 3 |
| Minimum unique queries | 3 |

**Actions:**

1. Score each candidate.
2. Promote passing candidates to L3 semantic memory.
3. Update L4 procedural memory with newly validated patterns or skills.
4. Reject or defer candidates that do not meet thresholds.

**Outputs:**

- New L3 facts and relationships
- Proposed L4 skill updates
- Rejection log for observability

---

## Phase 4: Prune — Fade & Archive

**Purpose:** Reduce noise and storage growth by applying differential forgetting.

**Actions:**

1. Apply exponential decay based on memory profile.
2. Move stale but not-yet-deleted memories to cold storage.
3. Archive pruned memories rather than deleting them outright (forensic / recovery value).

**Decay profiles (example):**

| Profile | Half-life | Use case | Example |
|---|---|---|---|
| Wine | 730 days | Core identity facts | "Agent name is Adaptoid." |
| Standard | 90 days | General knowledge | "User prefers dark mode." |
| News | 7 days | Transient information | "Weather forecast for today." |

**Outputs:**

- Updated retention metadata
- Cold-storage archive batch
- Storage-efficiency metrics

---

## Phase 5: Security Scan

**Purpose:** Detect anomalous write patterns that may indicate memory poisoning or adversarial input.

**Actions:**

1. Scan new and promoted memories for injection patterns.
2. Detect anomalous write rates or content signatures.
3. Flag and quarantine suspicious entries.
4. Emit a security report.

**Outputs:**

- Quarantine list
- Security report
- Alerts if thresholds are exceeded

---

## Phase 6: Self-Assessment

**Purpose:** Generate a concise summary of memory health and propose procedural updates.

**Actions:**

1. Compute a coherence score for the current memory state.
2. Log contradictions between self-knowledge and observed behavior.
3. Propose L4 updates if patterns warrant it.
4. Emit a "state of self" report.

**Outputs:**

- Coherence score
- Contradiction log
- Proposed L4 updates (subject to approval)

---

## Configuration Example

```yaml
consolidation:
  dream_cycle:
    trigger: on_idle  # on_idle | end_of_session | scheduled
    scheduled_time: "02:00"
    idle_threshold_minutes: 15

    phases:
      light_sleep:
        dedup_threshold: 0.9

      rem_sleep:
        pattern_min_occurrences: 3

      deep_sleep:
        min_score: 0.8
        min_recalls: 3
        min_unique_queries: 3
        weights:
          relevance: 0.30
          frequency: 0.24
          query_diversity: 0.15
          recency: 0.15
          consolidation: 0.10
          conceptual_richness: 0.06

      prune:
        archive_enabled: true
        profiles:
          wine: { half_life_days: 730 }
          standard: { half_life_days: 90 }
          news: { half_life_days: 7 }

      security_scan:
        enabled: true
        anomaly_threshold: 0.95

      self_assessment:
        enabled: true
        coherence_check: true
```

---

## Operational Notes

- **Keep it non-blocking.** The cycle must not stall user-facing requests.
- **Make thresholds configurable.** Different deployments have different noise tolerances.
- **Archive, do not delete.** Cold storage preserves forensic ability and allows rollback.
- **Require human approval for L4 changes.** Procedural memory changes behavior; guard them.
- **Do not anthropomorphize.** "Dream cycle" is a naming convention for batch maintenance, not a claim of cognition.
