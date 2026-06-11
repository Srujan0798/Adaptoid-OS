# Vault — Obsidian-Compatible Second Brain

> Human-facing knowledge store. Machine-parseable. Grep-friendly.

## Structure

```
vault/
├── daily/          — daily logs (YYYY-MM-DD.md)
├── projects/       — per-project notes
├── facts/          — verified facts (linked from memory-bank/)
├── decisions/      — ADR summaries
├── lessons/        — condensed lessons
├── graphs/         — Mermaid / DOT relationship diagrams
├── inbox/          — unprocessed captures
└── attachments/    — images, PDFs, screenshots
```

## Obsidian Integration
1. Open this folder as an Obsidian vault.
2. Enable the Graph view to see relationships.
3. Use `[[wikilinks]]` to connect concepts.

## Sync
`memory-sync.sh --index` rebuilds the SQLite FTS index over this vault.
