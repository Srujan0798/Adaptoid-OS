# Local Harness

> Optional local-first stack for Adaptoid OS. Sovereign: no cloud required.

## Quick Start

```bash
make up
```

This starts:
- **LiteLLM** (port 4000) — unified LLM gateway
- **Qdrant** (port 6333) — vector memory
- **Ollama** (port 11434) — local inference
- **Redis** (port 6379) — caching + pub/sub

## Status

```bash
make status
make health
```

## Teardown

```bash
make down
```

## Note
OS-Setup works without this stack. This is an optional accelerator.
