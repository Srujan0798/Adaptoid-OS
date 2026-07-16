# Agentic OS Profile — Local-First Harness (template)

> A starting template for a local-first agent harness: the "hands" + "knowledge" layer that an orchestrator drives. Linux primary (Ubuntu/Debian); macOS/Windows notes below. This is a TEMPLATE to adapt, not a claimed turnkey stack — verify each component for your environment.

## What a full local harness contains
```
┌──────────────────────────────────────────────────────────┐
│  ORCHESTRATOR  Claude Code / Kimi  (the brain)            │
└───────────┬──────────────────────────────────────────────┘
            │ drives via MCP + task files
   ┌────────┴──────────┬─────────────┬──────────────┐
   ▼                   ▼             ▼              ▼
 WORKERS            KNOWLEDGE       MEMORY         LOCAL LLM (optional)
 OpenCode CLI ×N    Obsidian vault  events.jsonl   Ollama (gpu/cpu)
 (parallel)         + graph (codegraph/Graphify)   for cheap/offline tasks
   │                                  + Letta/agentmemory (optional)
   ▼
 SANDBOX           OBSERVABILITY     DAEMON (optional)
 Docker exec       prometheus +      24/7 runner for long tasks
 (untrusted code)  logs              (systemd / pm2)
```

## Minimal docker-compose template (adapt; verify images/versions)
```yaml
# setup/docker-compose.agentic.yml — STARTING TEMPLATE
version: "3.9"
services:
  # Local LLM for cheap/offline worker tasks (optional)
  ollama:
    image: ollama/ollama:latest
    ports: ["11434:11434"]
    volumes: ["ollama:/root/.ollama"]
    # GPU: add deploy.resources.reservations.devices for nvidia

  # Vector/graph store for memory (optional — pick one)
  qdrant:
    image: qdrant/qdrant:latest
    ports: ["6333:6333"]
    volumes: ["qdrant:/qdrant/storage"]

  # Observability (T2+)
  prometheus:
    image: prom/prometheus:latest
    ports: ["9090:9090"]
    volumes: ["./prometheus.yml:/etc/prometheus/prometheus.yml"]

  # Sandbox for running untrusted worker-generated code (blast-radius containment)
  sandbox:
    build: { context: ., dockerfile: Dockerfile.sandbox }
    network_mode: none          # no network for untrusted exec
    read_only: true
    tmpfs: ["/tmp"]

volumes: { ollama: {}, qdrant: {} }
```

## One-command-ish bring-up (adapt)
```bash
# 1. Knowledge: init an Obsidian vault as the file-memory
mkdir -p vault && echo "# Project Brain" > vault/INDEX.md

# 2. Tools: declare MCP servers (the syscalls)
#    edit mcp.json (filesystem, git, tavily, context7, sequential-thinking, playwright)

# 3. Optional local stack
docker compose -f setup/docker-compose.agentic.yml up -d

# 4. Orchestrator: open Claude Code / Kimi in the project; it reads CLAUDE.md
# 5. Workers: open N OpenCode CLI windows; paste WORKER_PROMPT + a task brief each
```

## Platform notes
- **Ubuntu/Debian (primary):** native; Docker + Ollama + Node for OpenCode-class workers.
- **macOS:** same, Docker Desktop; Ollama native is faster than in-container on Apple Silicon.
- **Windows:** WSL2 strongly recommended; run the stack inside WSL.

## Security / sovereignty
- Untrusted worker code runs in the `sandbox` service (no network, read-only, tmpfs). Blast-radius containment.
- Secrets in `.env` (gitignored); never into worker containers (kernel ANTI-HALLUCINATION + FM-07).
- Local-first: nothing requires the cloud. Cloud is optional burst, not a dependency (sovereign-friendly).
- 24/7 daemon (optional): run the orchestrator loop under systemd/pm2 for long-horizon autonomy; gate r3+ actions for human approval (blast-radius.md).

## Honesty
This is a composition TEMPLATE drawn from the local-agent-OS ecosystem (gateway + channels + sandbox + vault + local LLM + observability patterns). Treat versions/images as starting points to verify, not guarantees. The orchestrator should confirm each component before relying on it (runtime-context-check discipline).
