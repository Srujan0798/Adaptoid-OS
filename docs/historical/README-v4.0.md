<div align="center">

# 🧠⚡ Adaptoid OS v4.0
## A Harness-First Agentic AI Operating System

[![Dogfood](https://img.shields.io/badge/dogfood-passing-brightgreen)](#)
[![Preflight](https://img.shields.io/badge/preflight-passing-brightgreen)](#)
[![Version](https://img.shields.io/badge/version-4.0-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)
[![Archetypes](https://img.shields.io/badge/archetypes-11-orange)](#)
[![Failure%20Modes](https://img.shields.io/badge/failure_modes-18-red)](#)

> **Adapt. Validate at runtime. Verify relentlessly. Compound carefully.**

**A framework-agnostic harness for agentic AI that treats the control stack surrounding the LLM — routing, memory, validation, policy — as the primary optimization target.**

[Quick Start](#quick-start) · [Features](#features) · [Comparison](#why-adaptoid-beats-every-alternative) · [Architecture](#architecture) · [Contributing](#contributing)

</div>

---

## The Problem

Agentic AI projects fail for the same 18 reasons, every time:
- Agents hallucinate DAG transitions and call wrong tools
- State drifts silently between sessions
- Workers claim "done" without evidence
- Context bloat causes遗忘 (forgetting)
- Embarrassing artifacts get committed to production
- No one knows what the active wave is after a crash

**Existing frameworks** (LangGraph, CrewAI, AutoGen) give you primitives. They don't give you an *operating system* that prevents, detects, and heals these failures automatically.

![Demo](docs/demo.gif)

---

## Quick Start

### Option A — One-Command Setup (Recommended)

```bash
curl -sSL https://raw.githubusercontent.com/Srujan0798/Adaptoid-OS/main/install.sh | bash
```

### Option B — Clone & Go

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git ~/adaptoid-os
cd ~/adaptoid-os
bash validators/dogfood.sh   # verify the kit
bash validators/preflight.sh # verify your project
```

### Option C — Engine-Driven (Sovereign, No AI Session Required)

```bash
python3 ~/adaptoid-os/adaptor/engine.py \
  --brief "Convert RFQ PDFs to structured BOQ" \
  --output ./my-project
```

The engine detects archetype, consults the ecosystem library, generates structure, copies validators, and runs preflight — all locally, no network, no AI session required.

---

## Features

<div align="center">

| 🔒 **Safety** | 🚀 **Speed** | 🧠 **Intelligence** |
|---|---|---|
| Route Sentinel (pre-execution blocking) | 11 archetypes = instant fit | Typed PROJECT-INTENT.md |
| VaultMMU (SHA-256 hash chain) | 5 core workflow templates | 18 failure modes with validators |
| OAP Security (deterministic policies) | Slash commands with cost caps | Self-improvement protocol (GEPA + Hermes) |
| 18 executable validators | Parallel conductor pattern | Living folder memory bank |

</div>

### Progressive Disclosure — The Actual Fix for "Agent Forgets Everything"

A single giant markdown bloats the context window. Agents read it once, then forget the middle, then contradict it.

**Adaptoid OS uses progressive disclosure:**
- **Kernel** (~2K tokens) — loaded every session
- **Protocols** — loaded on trigger
- **Failure Modes** — loaded when symptom appears
- **Ecosystem** — pulled like books from a shelf, then closed

---

## How Adaptoid Differs

Adaptoid OS is not a replacement for the frameworks below. It is a harness layer you can use with or without them.

| Dimension | LangGraph | CrewAI | AutoGen | **Adaptoid OS** |
|---|---|---|---|---|
| **Primary focus** | Stateful graphs | Role-based crews | Conversational agents | **Control stack / harness** |
| **Framework agnostic** | LangChain ecosystem | CrewAI | Microsoft ecosystem | ✅ **Sovereign core + optional bridges** |
| **Typed intent capture** | Manual | Manual | Manual | ✅ **PROJECT-INTENT.md + JSON Schema** |
| **Failure-mode library** | — | — | — | ✅ **18 FMs + validators** |
| **Deterministic safety layer** | Checkpoints | — | — | ✅ **Route Sentinel + VaultMMU + OAP** |
| **Living-folder memory** | In-graph | In-crew | In-chat | ✅ **Markdown + SQLite + Obsidian-ready** |
| **Self-validation** | — | — | — | ✅ **dogfood + preflight validators** |

**LangGraph** is excellent for durable, resumable graphs. Use Adaptoid's `claw_bridge/langgraph_adapter.py` when you want to export a plan to LangGraph.

**CrewAI** is great for quick role-based demos. Use the `crewai_adapter.py` when that model fits.

**AutoGen** shines for conversational multi-agent debate. Use the `autogen_adapter.py` for those waves.

**Adaptoid OS** focuses on the layer those frameworks do not: a failure-mode-aware control stack that stays independent.

---

## Architecture

```
┌─────────────────────────────────────────┐
│           ORCHESTRATOR                  │
│    (Claude Code / Kimi / Cursor)        │
│         Plans · Dispatches · Reviews    │
└──────────────┬──────────────────────────┘
               │ writes task brief
               ▼
┌─────────────────────────────────────────┐
│           WORKERS                       │
│    (OpenCode CLI / Codex / MiniMax)     │
│         Execute · Write code · Report   │
└──────────────┬──────────────────────────┘
               │ writes report
               ▼
┌─────────────────────────────────────────┐
│           VALIDATION LAYER              │
│  Route Sentinel · VaultMMU · OAP · L1-L7│
└─────────────────────────────────────────┘
```

**The 7-Layer Verification Stack:**
1. **L1** Schema validation (<50µs)
2. **L2** Deterministic / evidence grounding (<100µs)
3. **L3** LLM self-check
4. **L4** Critic / cross-verify
5. **L5** Source grounding / sandbox execution
6. **L6** VaultMMU state hash
7. **L7** Route Sentinel pre-route blocking

---

## Folder Map

```
adaptoid-os/
├── README.md                    ← you are here
├── AGENTS.md                    ← cold-start contract (read first!)
├── INDEX.md                     ← agent navigation table
├── 00-INVOCATION.md             ← paste-and-go prompt
├── CHANGELOG.md
│
├── kernel/                      ← ALWAYS loaded (~2K tokens)
│   ├── PRINCIPLES.md               12 non-negotiable laws
│   ├── TWO-TIER.md                 Brain/Hands/Session
│   └── ANTI-HALLUCINATION.md       drift prevention
│
├── philosophy/                  ← the Three Pillars
│   ├── LLM-as-OS.md
│   ├── freedom-responsibility.md
│   └── harness-engineering.md
│
├── patterns/                    ← 10 extracted best practices
│   ├── parallel-conductor.md
│   ├── six-enforced-questions.md
│   ├── closed-learning-loop.md
│   └── ...
│
├── failure-modes/               ← 18 real failures + prevention
│   ├── FM-01-state-drift.md
│   ├── FM-16-wrong-route.md
│   ├── FM-17-tampered-state.md
│   └── ...
│
├── protocols/                   ← load on trigger
│   ├── route-sentinel.md
│   ├── vault-mmu.md
│   ├── oap-security.md
│   ├── self-improvement.md
│   └── ...
│
├── archetypes/                  ← 11 adaptation profiles
├── workflows/                   ← 5 core + 8 domain YAML
├── slash-commands/              ← named orchestrator API
├── memory-bank/                 ← living folder memory
├── validators/                  ← 20 executable scripts
├── templates/                   ← project skeleton
├── reference/ecosystem/         ← DevKit library
├── setup/harness/               ← Docker Compose stack
└── schemas/                     ← JSON Schema specs
```

---

## The Core Loop

```
read kernel/ → detect archetype → pick tier → generate structure
     → run validators/preflight.sh → dispatch wave-1 → workers execute
     → review (evidence required) → merge → ship → next wave
     → on ANY anomaly: consult failure-modes/ → add validator
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Every critical bug found in production → add a new FM file + regression test + validator.** The library only grows.

---

## License

MIT — see [LICENSE](LICENSE)

---

<div align="center">

**⭐ Star this repo if it saves you from one agentic failure.**

*Built from 5 real shipping projects + 300+ research sources + 97 gap analyses. Not theory. Battle-tested.*

</div>
