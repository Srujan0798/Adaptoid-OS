# 🛠️ MASTER-SETUP.md

> *The single source of truth for "how is the Adaptoid-OS stack wired". Read
> this after AGENTS.md, after ADAPTOID-ENGINE.md, after
> VERIFICATION-PROTOCOLS.md, and after PROJECT-INTENT.md. This file is what
> `bootstrap.sh` reads to bring the OS up.*

---

## 0. The thesis

> The Adaptoid-OS stack is **one Docker Compose file, one bootstrap script,
> one .env file, and one set of opinionated defaults** — open, swappable, and
> verifiable. You can be productive in 90 seconds, and you can replace any
> layer without breaking the others.

The stack is **MCP-first**, **OpenTelemetry-native**, **LiteLLM-routed**,
**local-LLM-friendly**, and **durable-execution-ready**. It is the only stack
that ships with all of those defaults *and* the verification regime to keep
them honest.

---

## 1. The default stack (mid-2026)

| Layer                 | Default                                       | Alternative(s)                              | Notes                                                  |
| --------------------- | --------------------------------------------- | ------------------------------------------- | ------------------------------------------------------ |
| LLM gateway           | **LiteLLM** (1.40+)                           | OpenRouter, Portkey, custom                 | One endpoint, all providers                            |
| Local LLM             | **Ollama** (0.5+)                             | vLLM, LM Studio, llama.cpp                  | Auto-warm at bootstrap                                 |
| Cloud LLM             | **OpenAI** + **Anthropic** + **Google**       | Azure OpenAI, Bedrock, Vertex               | Set keys in `.env`                                     |
| Orchestration         | **LangGraph** (0.3+)                          | OpenAI Agents SDK, Claude Agent SDK, Agno   | Reference runtime uses LangGraph                        |
| Structured outputs    | **Pydantic AI** (1.0+)                        | BAML, Instructor, Outlines                  | Pydantic AI is the default; BAML for multi-lang        |
| Protocol: tool use    | **MCP** (1.0+, Linux Foundation Agentic AI Foundation) | Function calling (legacy)         | Every claim about a system is bound to an MCP call     |
| Protocol: multi-agent | **A2A** (Google)                              | Direct, in-process, ACP (IBM)               | Used when 2+ Adaptoids are in play                     |
| Skills                | **Anthropic Agent Skills** (open standard)    | Hand-rolled prompts, function-calling       | Folder-based, versioned, testable                      |
| Memory: working       | **In-context + state graph**                  | —                                           | Layer 1 in `MEMORY-INDEX.md`                           |
| Memory: semantic      | **Qdrant** (default), **Weaviate** / **pgvector** | Pinecone, Chroma                        | Layer 2                                                 |
| Memory: episodic      | **Letta** (default) / **Zep (Graphiti)**      | Mem0, Cognee                                | Layer 2 (graph)                                         |
| Memory: bank          | **Markdown + SQLite FTS**                     | —                                           | The Adaptoid-specific durable bank                      |
| Durable execution     | **Inngest** (default for events)              | Temporal, Restate, DBOS                     | Pick per task; see `preferences.durable_exec`           |
| Observability         | **Langfuse** (default)                        | LangSmith, Logfire, Phoenix, Arize          | All OTel-native                                        |
| Eval                  | **Promptfoo** + **DeepEval** + calibration set| Inspect (UK AISI), custom                   | Calibrated to local holdout                             |
| Browser use           | **Browser-Use** / **Stagehand**               | Anthropic Computer Use, OpenAI Operator     | Optional, MCP-served                                    |
| Editor                | **VS Code** + **Cursor** + **Claude Code**    | JetBrains, Zed                              | Configs ship in `config/`                              |
| Terminal              | **tmux** / **zellij** layouts                  | iTerm2, WezTerm                             | Layouts in `config/terminal/`                          |
| Secret mgmt           | **1Password CLI** / **sops** / **age**        | HashiCorp Vault, Doppler                    | Pick one; never commit secrets                          |

The **Adaptoid is opinionated about the protocol layers (MCP, A2A, Skills,
OTel, OpenAPI) and the verification layers (Pydantic AI / BAML, evidence,
route, cross-check).** Everything else can be swapped via `profiles/`.

---

## 2. The directory layout (the living folder)

The default install creates:

```
<project-root>/
├── adaptoid/                          # ← the DevKit lives here
│   ├── README.md
│   ├── MASTER-SETUP.md
│   ├── ADAPTOID-ENGINE.md
│   ├── VERIFICATION-PROTOCOLS.md
│   ├── PROJECT-INTENT.md             # ← user fills this in
│   ├── MEMORY-INDEX.md
│   ├── AGENTS.md
│   ├── docker-compose.yml
│   ├── .env.example
│   ├── scripts/                      # bootstrap, verify, memory-sync, intent-parse
│   ├── config/                       # claude-code/, vscode/, terminal/
│   ├── skills/                       # core, domain, templates
│   ├── workflows/                    # parallel, long-horizon, verification, examples
│   ├── adapters/                     # problem-adapter, intent-parser, failure-mode-mapper
│   ├── examples/                     # hackathon, production, research, bug-fix, data-pipeline
│   ├── references/                   # landscape-map, headroom-analysis, bibliography
│   ├── profiles/                     # conservative, balanced, aggressive
│   ├── memory-bank/                  # ← grows organically
│   ├── reports/                      # eval-*.md, benchmark-*.md
│   └── logs/
├── .adaptoid/                         # hidden runtime state
│   ├── ci/                           # CI hooks
│   ├── cache/                        # model cache, evidence cache
│   └── runtime/                      # controller state, plan traces
└── <your project>                    # your actual project
```

The DevKit is **isolated in `adaptoid/`** so you can lift it in and out, version
it independently, and keep your project tree clean.

---

## 3. The bootstrap (`scripts/bootstrap.sh`)

```bash
# Default install (Ubuntu / macOS / WSL2)
./adaptoid/scripts/bootstrap.sh

# Idempotent — safe to re-run
./adaptoid/scripts/bootstrap.sh

# Pick a profile
./adaptoid/scripts/bootstrap.sh --profile conservative
./adaptoid/scripts/bootstrap.sh --profile aggressive

# Skip Docker stack (local-only mode)
./adaptoid/scripts/bootstrap.sh --no-docker

# Init a new project
./adaptoid/scripts/bootstrap.sh --init
```

What the script does (in order, with `--explain` for verbose output):

1. **Preflight**: detect OS, architecture, container runtime (Docker /
   OrbStack / Colima / Rancher Desktop / Podman), Python (3.11+), Node (20+),
   git, curl.
2. **Secrets**: check `.env` for required keys; prompt if missing; never log
   values.
3. **Container stack**: `docker compose -f adaptoid/docker-compose.yml up -d`.
4. **Local LLM**: if `preferences.local_runtime: ollama`, install Ollama,
   pull the primary model, **warm it up** (a 1-token completion to mmap-cache
   it).
5. **Skills sync**: `git submodule update --init` if a private skills repo is
   configured; otherwise copy the bundled core set.
6. **Memory bank init**: create `memory-bank/` if missing, initialize the SQLite
   FTS index.
7. **Hooks install**: drop session-start and session-end hooks into
   `~/.claude/`, `~/.codex/`, `~/.cursor/`, `~/.continue/` (best-effort, only
   the ones present).
8. **Editor config**: symlink `config/vscode/settings.json` and
   `config/vscode/mcp.json` into `.vscode/` if present.
9. **Self-verify**: run `scripts/verify-setup.sh` and report.
10. **Print the cold-start contract** to the terminal.

The script is **idempotent**: re-running it is a no-op except for upgrades and
re-verify.

---

## 4. The Docker Compose stack (`docker-compose.yml`)

The compose file wires the default services. Each service is **small,
scoped, and OTel-instrumented**. The file is well-commented so you can edit
it confidently.

Services:

- `litellm` — the gateway. Routes to Ollama, OpenAI, Anthropic, Google, etc.
  OTel-instrumented. Healthcheck on `/health`.
- `ollama` — local LLM runtime. Pulls models declared in `.env`. Volume
  `ollama_data` for persistence.
- `qdrant` — vector store for semantic memory. Volume `qdrant_data`.
- `letta` — episodic / graph memory. Persists to Postgres.
- `postgres` — backing store for Letta, Temporal, the Adaptoid state.
- `langfuse` — LLM observability. Single-container mode.
- `langfuse-worker` — async ingestion worker for Langfuse.
- `inngest` — durable execution server (dev mode).
- `temporal` — durable execution server (alternative, opt-in).
- `mcp-memory-server` — Adaptoid's MCP server exposing `memory-bank/` over
  MCP (read/write/search).
- `mcp-filesystem` — Adaptoid's MCP server for safe filesystem access.
- `mcp-git` — Adaptoid's MCP server for git operations.
- `mcp-shell` — Adaptoid's MCP server for sandboxed shell.
- `redis` — cache + queue for Inngest.
- `adaptoid-controller` — the Adaptoid Engine runtime (LangGraph-based).
- `adaptoid-verify` — verification sidecar (Promptfoo, DeepEval, calibration).
- `adaptoid-memviz` — memory graph web viewer (dev only).

Each service is **independently startable**:

```bash
docker compose up -d litellm qdrant
docker compose --profile durable up -d temporal
```

Profiles:

- `default` — the median setup (gateway + memory + observability + controller).
- `durable` — adds Temporal / Inngest for long-horizon.
- `local-only` — no cloud LLM deps; everything runs on Ollama.
- `prod` — same as `default` + TLS, secrets via sops, no `:latest` tags.
- `reg` — adds the Adaptoid Registry (private skill store).

---

## 5. The `.env.example`

Documented, never logged. Keys:

```bash
# Core
ADAPTOID_ENGINE_VERSION=1.0.0
ADAPTOID_PROFILE=balanced
ADAPTOID_INTENT_PATH=adaptoid/PROJECT-INTENT.md
ADAPTOID_MEMORY_PATH=adaptoid/memory-bank

# LLM gateway
LITELLM_MASTER_KEY=sk-adaptoid-...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
GROQ_API_KEY=...

# Local LLM
OLLAMA_HOST=http://ollama:11434
OLLAMA_PRIMARY=llama3.1:8b-instruct-q5_K_M
OLLAMA_FALLBACK=qwen2.5:7b-instruct-q5_K_M

# Memory
QDRANT_URL=http://qdrant:6333
LETTA_URL=http://letta:8283
LETTA_PASSWORD=...

# Durable exec
INNGEST_DEV=http://inngest:8288
TEMPORAL_ADDRESS=temporal:7233

# Observability
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=http://langfuse:3000
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317

# Calibration / eval
ADAPTOID_CALIBRATION_SET=adaptoid/calibration/

# Secrets manager (pick one)
SECRETS_BACKEND=op           # op | sops | age | vault | doppler

# Domain
DOMAIN=code                  # code | research | data | ops | product | creative | hybrid
DATA_SENSITIVITY=public      # public | internal | confidential | regulated
COMPLIANCE=
```

`bootstrap.sh` checks that all required keys are present; `verify-setup.sh`
exercises each service end-to-end.

---

## 6. The profiles (`profiles/`)

Profiles are *typed overrides* on the default engine config. Three shipped
profiles; the user can add more.

```yaml
# profiles/balanced.yaml  (default)
risk_tolerance: balanced
cost_ceiling_per_node_usd: 0.10
escalation_threshold: 0.45
verification: [type_check, evidence_grounding]
human_in_loop: false
auto_rollback: true
```

```yaml
# profiles/conservative.yaml
risk_tolerance: conservative
cost_ceiling_per_node_usd: 0.05
escalation_threshold: 0.30
verification: [type_check, evidence_grounding, cross_check]
human_in_loop: true
auto_rollback: true
```

```yaml
# profiles/aggressive.yaml
risk_tolerance: aggressive
cost_ceiling_per_node_usd: 0.30
escalation_threshold: 0.60
verification: [type_check]
human_in_loop: false
auto_rollback: false   # ← user is on the hook
```

A profile is **the personality of the controller**, not the model choice.
Model choice is in `preferences.llm` of `PROJECT-INTENT.md`.

---

## 7. Platform variants

The same DevKit works on:

- **Linux / Ubuntu 22.04+ / Debian 12+** — primary target. Docker, Ollama,
  full stack.
- **macOS 14+ (Apple Silicon)** — Docker via OrbStack (recommended) or
  Colima. Ollama native, very fast on M-series. Some services (Temporal) work
  on ARM.
- **Windows 11 (WSL2)** — install Ubuntu 22.04 in WSL2, then it's the same
  as Linux. GPU passthrough for Ollama is experimental.
- **Headless / CI** — `--no-docker --no-editor` flags. Used in
  `examples/production/`.

The bootstrap detects the platform and adjusts.

---

## 8. GPU / local LLM

```bash
# NVIDIA GPU passthrough
docker compose --profile gpu up -d ollama
# In compose: deploy.resources.reservations.devices with driver: nvidia

# Apple Silicon — Ollama runs natively on the host
OLLAMA_HOST=http://host.docker.internal:11434
docker compose up -d litellm qdrant postgres
ollama serve &  # on the host

# CPU-only fallback
docker compose up -d ollama    # will be slow on CPU; not recommended for prod
```

The `OLLAMA_PRIMARY` model in `.env` is the default; the controller
auto-downgrades if it's not pulled.

---

## 9. The verification sidecar (`adaptoid-verify`)

A small service that runs:

- `Promptfoo` evals against the calibration set
- `DeepEval` metric assertions
- The OTel collector for trace aggregation
- A nightly Skill-rot check (`last_verified` < ttl)

It exposes a `/healthz` and a `/report` endpoint. The CI hooks
(`.adaptoid/ci/`) call it on every PR.

---

## 10. Upgrading the stack

```bash
# Pull latest DevKit
git pull
./adaptoid/scripts/bootstrap.sh

# Check version
./adaptoid/scripts/bootstrap.sh --version

# Migrate (if major version bump)
./adaptoid/scripts/migrate.sh
```

Major-version bumps come with a `MIGRATION.md`. The bootstrap refuses to
proceed on a breaking change without it.

---

## 11. The "is it working?" checklist

After `bootstrap.sh`, you should see:

- [ ] `docker compose ps` shows all services `running` (or `running (healthy)`)
- [ ] `curl http://localhost:4000/health` (LiteLLM) returns 200
- [ ] `curl http://localhost:6333/health` (Qdrant) returns 200
- [ ] `curl http://localhost:3000/api/public/health` (Langfuse) returns 200
- [ ] `python adaptoid/scripts/intent-parse.py --check` exits 0
- [ ] `./adaptoid/scripts/verify-setup.sh` exits 0
- [ ] `cat adaptoid/memory-bank/INDEX.md` is non-empty
- [ ] `claude --project-dir .` loads the cold-start contract

If any of these fail, `./adaptoid/scripts/bootstrap.sh --explain --verbose`
will print the diagnostic.

---

## 12. The "I want to swap a layer" guide

Swap the LLM gateway (LiteLLM → Portkey):

1. Stop `litellm`: `docker compose stop litellm`.
2. Add `portkey` to `docker-compose.yml` (see `examples/production/`).
3. Update `LITELLM_MASTER_KEY` → `PORTKEY_API_KEY` in `.env`.
4. Restart: `docker compose up -d portkey`.
5. The controller talks to `http://gateway:4000/v1` regardless.

Swap Letta → Mem0:

1. Stop `letta`.
2. Add `mem0` to compose (the Adaptoid ships a `mem0` service in
   `examples/production/`).
3. Update `LETTA_URL` → `MEM0_URL` in `.env`.
4. The MCP memory server proxies through.

Swap Inngest → Temporal:

1. `docker compose --profile durable up -d temporal`.
2. Update `preferences.durable_exec: temporal` in `PROJECT-INTENT.md`.
3. The controller re-emits durable nodes accordingly.

Every swap is **additive, observable, and reversible**. The Adaptoid
verification regime is unchanged.

---

## 13. TL;DR

> One `docker-compose.yml`, one `bootstrap.sh`, one `.env`, one set of
> opinionated defaults, one verification regime, one cold-start contract. The
> DevKit is the floor; the user owns the rest. Swap any layer without
> breaking the others. Be productive in 90 seconds. Be production-grade
> without a re-architecture.

🜂
