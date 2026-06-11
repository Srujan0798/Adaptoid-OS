---
last-verified: 2026-06-11
confidence: corpus
---

# Ecosystem — SELECTION (archetype → recommended stack)

> The decision engine. After archetype + tier are chosen, this maps to a concrete tool/pattern stack. The orchestrator uses it, records picks as an ADR, then wires them in. Defaults are sane; override per project.

## Universal baseline (every project, every archetype)
- **Standards:** MCP (`mcp.json`) + agentskills.io skills + AGENTS.md/CLAUDE.md alias. Always.
- **Orchestrator:** Claude Code ⇄ Kimi (interchangeable).
- **Workers:** OpenCode CLI (or chosen) in parallel.
- **Optimizations:** prompt caching + progressive disclosure always; add compression/indexing as size grows.
- **Verification:** eval/acceptance contracts + Swiss-cheese + validators/preflight.

## Per-archetype stack

### hackathon
- MCP: filesystem, git, (maybe playwright for a web demo)
- Skills: tdd-lite, code-review; whatever the demo needs
- Optimizations: prompt caching; skip the rest
- Memory: none (in-session)
- Skip: SDKs/ADKs, multi-agent frameworks, knowledge systems

### internship / job-take-home
- MCP: filesystem, git, context7 (docs)
- Skills: tdd, code-review, diagnose, to-prd
- Optimizations: caching, deterministic tests
- Knowledge: NotebookLM/Obsidian for the report's lit/context (internship)
- Publish gate HARD (FM-07) — no artifacts in the reviewed repo
- Skip: SDKs/ADKs unless the deliverable IS an agent

### research-ml
- MCP: filesystem, git, tavily (papers)
- Knowledge: NotebookLM + Obsidian (read the 10 refs), markitdown (normalize PDFs)
- Memory/context: codegraph if large codebase
- Optimizations: caching; one-source metrics; config-as-law assertions
- Eval: experiments-as-evals, pass^k ≈ seed stability
- Skip: UI frameworks, multi-tenant, SDKs

### nlp-pipeline
- Ingestion: markitdown / pdfplumber / Tesseract / PaddleOCR / LayoutParser
- Knowledge: hybrid RAG (semantic + keyword), schema-first extraction
- Context: codegraph for the codebase
- Skills: pdf-processing, excel-processing
- Eval: golden set; F1 from one source
- Skip: multi-tenant, billing

### internal-tool
- Stack: FastAPI/Django + Postgres + React (or chosen)
- MCP: filesystem, git, serena (code), playwright (e2e)
- Optimizations: caching, parallel workers (disjoint waves)
- Tier: T1→T2; add observability when daily users
- Skip: SDKs/ADKs, personal-agent tools

### saas-product / startup-mvp
- Stack: prod web stack + auth + multi-tenant (saas) / lean (mvp)
- Memory: Letta/Mem0 if per-user agent memory; agentmemory for coding-agent recall
- Optimizations: caching + headroom (cut inference cost 60–95%) + codegraph
- Observability: prometheus, SLOs (T2+); compliance (T3)
- Analytics: funnel instrumentation (mvp)
- If it's an agent product: pick an SDK/ADK (sdks-adks.md)

### cli-tool
- MCP: filesystem, git
- Skills: tdd, code-review; matrix CI
- Optimizations: minimal deps; caching
- Skip: everything heavy

### data-pipeline
- Stack: Airflow/dbt or chosen; warehouse
- Quality: data contracts, quarantine + alert (FM-11)
- Optimizations: idempotency, one transformation layer for metrics
- Skip: UI beyond dashboard, SDKs

### personal-assistant product
- Base: OpenClaw or Hermes or nanobot (personal-agents.md)
- Memory: Letta + Honcho-style user modeling
- Channels: chat-app adapters
- Standards still apply (MCP, skills)

## Always record the decision
For each project, write `docs/decisions/0002-stack-selection.md`: chosen tools + the one-line why for each + what was rejected. This is the ADR that makes the choice auditable and prevents re-litigating it (and prevents FM-09 hand-waving).

## The meta-rule
Pull the SMALLEST stack that ships the archetype. Every tool is a liability (deps, context, failure surface). The library is big so you can CHOOSE well, not so you use it all.
