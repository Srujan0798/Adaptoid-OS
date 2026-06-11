# Ecosystem — Knowledge Systems & RAG (second brain, docs, retrieval)

> Pull when the project is knowledge-heavy: research, docs, RAG, "talk to my notes/corpus," or when the agent needs grounded external knowledge.

## Personal knowledge / second brain
| Tool | What | Pick when | Source |
|---|---|---|---|
| **Obsidian + Smart Connections** | local-first notes; embeddings; Smart Chat/Context/Environment; chat-with-your-vault | personal knowledge base the agent can query | github.com/brianpetro/obsidian-smart-connections (corpus) |
| **NotebookLM** | Google; source-grounded chat + audio overviews; "thinking partner" | grounded Q&A over a fixed source set; research synthesis | notebooklm (corpus) |
| **knowledge-work-plugins** | ⚡ open Claude plugins for knowledge workers | extend Claude for non-code knowledge work | github ⚡ |

## Document → LLM prep
| Tool | What | Source |
|---|---|---|
| **markitdown** | ⚡ any file (PDF/Office/HTML/images) → clean Markdown | github/microsoft ⚡ |
| **pdfplumber / Tesseract / PaddleOCR / LayoutParser** | proven ingestion stack: digital + scanned + layout | (corpus, proven in nlp-pipeline projects) |
| **codegraph / Understand-Anything** | ⚡ code → knowledge graph (RAG over a codebase) | github ⚡ |

## Code/repo knowledge graphs (the "graph memory" layer)
| Tool | What | Pick when | Source |
|---|---|---|---|
| **Graphify** | knowledge-graph builder for coding assistants: Tree-sitter AST + LLM → NetworkX graph, Leiden clustering, "god nodes"/surprise analysis, exports to Obsidian/HTML/JSON; integrates with coding agents | give an agent a structured map of a large/unfamiliar codebase instead of raw file reads | community-reported; verify repo before relying |
| **codegraph** | ⚡ pre-indexed code knowledge graph for Claude Code/Codex/Gemini/Cursor | same, multi-agent compatible, trending | github ⚡ |
| **InfraNodus-style gap analysis** | graph + gap/blind-spot analysis over a knowledge base | find what's MISSING in a corpus/codebase | community-reported; verify |

> The pattern these establish: **graph memory** — instead of dumping files into context, build a navigable graph (entities, relations, clusters) the agent queries. Pairs with Obsidian (export the graph to the vault) and the memory-context tools. This is the upper end of FM-04 (context) mitigation for large codebases/corpora.

## RAG patterns (2026)
1. **Index, don't dump** — embeddings + retrieval, not whole-corpus-in-context.
2. **Ground + cite** — every answer carries sources; no source = don't assert (anti-hallucination).
3. **Hybrid retrieval** — semantic + keyword (BM25/FTS) beats either alone.
4. **Quality gate** — low-confidence retrieval → manual review queue, never silent wrong (FM-11).
5. **Schema-first extraction** — define the target schema, validate before use (your rfq2boq lesson).

## How OS-Setup uses this
- `nlp-pipeline` archetype pulls this file by default.
- `research-ml` uses NotebookLM/Obsidian as the "read the 10 papers" thinking layer feeding the lit-review.
- Any project with a docs corpus: markitdown to normalize → embed → retrieve, with grounding + citations.
- Second-brain pattern (Obsidian + Smart Connections) is the optional `/second-brain` capability for the orchestrator to query accumulated project knowledge.

`verified: 2026-05 (markitdown, knowledge-work-plugins, codegraph ⚡; Obsidian/NotebookLM corpus)`
