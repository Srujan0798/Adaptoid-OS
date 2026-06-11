<div align="center">

# 🧠⚡ Adaptoid OS v4.0
## The Eternal Universal Agentic AI Harness

[![Dogfood](https://img.shields.io/badge/dogfood-passing-brightgreen)](#)
[![Preflight](https://img.shields.io/badge/preflight-passing-brightgreen)](#)
[![Version](https://img.shields.io/badge/version-4.0-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)
[![Archetypes](https://img.shields.io/badge/archetypes-11-orange)](#)
[![Failure%20Modes](https://img.shields.io/badge/failure_modes-18-red)](#)

> **Adapt. Validate at runtime. Verify relentlessly. Compound eternally.**

**A self-improving, framework-agnostic operating system for agentic AI that treats harness engineering — the control stack surrounding the LLM — as the primary optimization target.**

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

## Why Adaptoid Beats Every Alternative

| Dimension | LangGraph | CrewAI | AutoGen | **Adaptoid OS** |
|---|---|---|---|---|
| **Framework Agnostic** | ❌ LangChain-only | ❌ CrewAI-only | ❌ Microsoft ecosystem | ✅ **Sovereign meta-core** |
| **Self-Improving** | ❌ | ❌ | ❌ | ✅ **GEPA + Hermes loops** |
| **Deterministic Safety** | Partial | ❌ | ❌ | ✅ **Route Sentinel + VaultMMU + OAP** |
| **Typed Intent Capture** | ❌ | ❌ | ❌ | ✅ **PROJECT-INTENT.md + JSON Schema** |
| **Failure Mode Library** | ❌ | ❌ | ❌ | ✅ **18 FMs with executable validators** |
| **Living Folder Memory** | ❌ (in-memory) | ❌ (crew only) | ❌ | ✅ **Markdown + SQLite + Obsidian** |
| **Cost Caps** | ❌ | ❌ (30% overhead) | ❌ (5-10x overrun) | ✅ **Per-command ceilings** |
| **One-Command Setup** | ❌ | ❌ | ❌ | ✅ **`install.sh`** |
| **Dogfood Validation** | ❌ | ❌ | ❌ | ✅ **Kit validates itself** |

**LangGraph** (~85K stars): Best for regulated industries with deterministic graphs. Steep learning curve, no self-improvement.

**CrewAI** (~46K stars): Fastest to demo. Role-based collaboration. Fractures after ~40 production runs.

**AutoGen** (~36K stars): Microsoft's enterprise framework. Azure-dependent, no built-in verification.

**Adaptoid OS**: The first system built from the ground up with harness engineering as its *raison d'être*.

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
