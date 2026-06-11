# Adaptor Example — Brief → Tailored Output

> A worked example of the engine transforming a brief into executable artifacts. Generic; illustrative.

## Input brief
```
Build a tool that ingests messy supplier invoices (PDF, some scanned) and outputs
a clean structured ledger (vendor, line items, totals, tax) for an accounting team.
Context: deadline 3 weeks · audience: internal finance team · tech: you choose ·
must-not-do: don't auto-post to the accounting system, output a reviewable file.
Success: 90% line accuracy on a held-out set, runs on one document in <30s.
```

## Engine pass

**ANALYZE** → archetype = `nlp-pipeline` (extraction + OCR + schema); tier = T2 (real users, accuracy target, but internal). Highest-risk FMs: FM-11 (silent fallback to wrong data), FM-05 (accuracy stated two ways), FM-10 (flaky extraction tests), FM-02 (model runs).

**PULL** →
- SELECTION nlp-pipeline stack: markitdown + pdfplumber + Tesseract/PaddleOCR + LayoutParser; hybrid RAG; schema-first; golden set.
- skills: `pdf-processing`, `excel-processing`, `tdd`, `code-review`.
- workflows: `graph-synthesis` not needed; use `planner-coder-reviewer` + `self-healing-verify`.
- validators: publish_gate, check_silent_failures, check_metrics, validate_state, preflight.

**COMPOSE** (excerpt of emitted `workflows/invoices.plan.yaml`)
```yaml
archetype: nlp-pipeline
tier: T2
stack: [markitdown, pdfplumber, tesseract, layoutparser, pydantic, fastapi]
waves:
  - id: wave-1   # ingestion + schema
    parallelism: 3
    tasks:
      - id: 01-ingest
        writes: [src/ingest/loader.py, tests/test_loader.py]
        skills: [pdf-processing, tdd]
        acceptance: "pytest tests/test_loader.py"
        blast_radius: r1
      - id: 02-schema
        writes: [src/schema/ledger.py, tests/test_schema.py]
        skills: [tdd]
        acceptance: "pytest tests/test_schema.py"
    gates: {pre_merge: [preflight.sh]}
    self_heal: {on_acceptance_fail: revise_brief}
  - id: wave-2   # extraction + golden set
    tasks:
      - id: 01-extract
        writes: [src/extract/ner.py, tests/golden/]
        acceptance: "pytest tests/golden/  # F1>=0.90"
        self_heal: {on_flaky: quarantine_and_fix}   # FM-10
```

**RECORD** → `docs/decisions/0002-stack-selection.md`: "Chose Tesseract+PaddleOCR over a cloud OCR API because must-run-local + cost; rejected pure-LLM extraction (hallucinates on contracts — FM-11); schema-first + golden set to hold the 90% line."

**VERIFY** → `preflight.sh` green → wave-1 task files ready.

## Output the human sees
```
Created: invoices/ (nlp-pipeline, T2)
Stack: markitdown · pdfplumber · Tesseract/PaddleOCR · LayoutParser · Pydantic · FastAPI
Wave-1 ready: work/wave-1/{01-ingest, 02-schema}.md
Validators wired: publish_gate, check_silent_failures, check_metrics, preflight
Highest-risk FMs guarded: FM-11 (no silent fallback), FM-05 (accuracy from one source), FM-10 (golden determinism)
Start: open Claude Code → /dispatch wave-1 → paste briefs into OpenCode workers
```

## What made it "tailored"
Same DevKit, but this project got: OCR stack (not a web stack), golden-set determinism (because accuracy target), FM-11 hard-wired (because "don't output wrong data silently" is the real risk), and a <30s perf gate — none of which a generic template would have chosen. That selection is the Adaptor doing its job.
