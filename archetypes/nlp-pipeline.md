# Archetype — NLP / Document Extraction Pipeline

**Signals.** "NER", "OCR", "extraction", "parse documents", "PDF→structured", "entities/relations", "ontology", "BOQ/RFQ/invoice/resume parsing". (rfq2boq type.)

**Default tier.** T1→T2 depending on whether it ships to users.

## Emphasize
- **Ingestion robustness.** Real documents are messy: scanned, mixed-layout, multi-language. Quality gate routes low-confidence inputs to a manual queue rather than guessing.
- **Schema-first output.** Define the target schema (Pydantic) before extraction. Validate before any downstream use. Reject malformed loudly (FM-11).
- **Golden test set.** A fixed set of input docs → expected structured output. Breaks if the parser drifts. This is your regression backbone.
- **Hybrid > pure-LLM.** Rules/ontology validator approves entities; pure-LLM hallucinates on contracts. Confidence scores + missing-item warnings, never silent drops.
- **Annotation + IAA.** If training a model, track inter-annotator agreement; version the gold set.

## Skip (unless asked)
- Multi-tenancy, billing
- Heavy UI (a review queue is enough)

## Folders
- Include: `src/{ingest,preproc,nlp,extraction,ontology,rules,export,evaluation}`, `data/{raw,samples,synthetic,annotations,gold,ontology}`, `tests/{unit,integration,golden}`, `models/` (if training), `schema/`, `evals/` (extraction accuracy as eval tasks).
- `docs/`: data_collection, annotation_guide, schema, conventions.

## Highest-risk failure modes
- **FM-11 silent failures** — NEVER fall back to synthetic data silently; a missing real corpus must fail loud (this exact guard mattered in rfq2boq).
- **FM-05 metric inconsistency** — F1/precision/recall from one generated source.
- **FM-10 flaky tests** — golden tests must be deterministic (seed any model inference).
- **FM-02 stale process** — model training runs: one at a time, params asserted.
- **FM-12 stale derived docs** — accuracy numbers in README regenerated.

## Definition of done
- Pipeline: real document in → validated structured output out, end-to-end
- Golden set passes; F1/coverage meet the target in PRD
- Low-confidence inputs routed to manual queue, not silently wrong
- Every metric from one source

## Deliverables
- The pipeline + API/CLI
- Golden eval results
- Annotated corpus (if applicable)
- Report (if internship/research flavored)
