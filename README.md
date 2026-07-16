<div align="center">

# Adaptoid OS v5.0
## An Agent Operating System for Agentic AI

[![Dogfood](https://img.shields.io/badge/dogfood-passing-brightgreen)](#)
[![Preflight](https://img.shields.io/badge/preflight-passing-brightgreen)](#)
[![Version](https://img.shields.io/badge/version-5.1-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)
[![Archetypes](https://img.shields.io/badge/archetypes-11-orange)](#)
[![Failure%20Modes](https://img.shields.io/badge/failure_modes-18-red)](#)

> **Adapt. Validate at runtime. Verify relentlessly. Compound carefully.**

**A framework-agnostic harness that helps turn LLMs into a self-monitoring, self-improving, wrong-route-blocking agentic workforce.**

[Quick Start](#quick-start) · [Features](#features) · [Comparison](#why-adaptoid-os-wins) · [Architecture](#architecture) · [v5.0 Protocols](#v50-protocol-layer) · [Contributing](#contributing)

</div>

---

## The Problem

Agentic AI projects fail for the same 18 reasons, again and again:

- Agents hallucinate DAG transitions and call the wrong tools.
- State drifts silently between sessions.
- Workers claim "done" without evidence.
- Context bloat causes forgetting.
- Embarrassing artifacts get committed to production.
- No one knows what the active wave is after a crash.
- Duplicate or contradictory rows appear in state files.
- Old processes run with wrong parameters.
- Documentation links point nowhere.
- Metrics are stated two different ways.
- Configs silently revert.
- Errors are swallowed by fallback code.
- READMEs show stale results.
- Two workers edit the same file.
- New sessions have no idea where things are.
- Orchestrators hit token limits and lose state.
- Routes are tampered with or undetected.
- Unauthorized tool calls cause destructive actions.

**Existing frameworks** (LangGraph, CrewAI, AutoGen) give you primitives. Adaptoid OS adds the control stack that helps prevent, detect, and heal these failures before they ship.

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
# Pro kit (full) + Claude + AGENTS.md hosts
python3 ~/adaptoid-os/adaptor/engine.py \
  --brief "Convert RFQ PDFs to structured BOQ" \
  --output ./my-project \
  --host agents,claude

# Core kit only — minimum portable harness for any host
python3 ~/adaptoid-os/adaptor/engine.py \
  --brief "48h hackathon: collab whiteboard" \
  --output ./hack \
  --core-only \
  --host all
```

The engine detects archetype, emits **host adapters** (`AGENTS.md`, `CLAUDE.md`, Cursor rules, …), copies Core or Pro validators, and runs preflight — all locally, no network, no AI session required.

### Product ladder

| Layer | Path | Use when |
|---|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` | One paste into any chat |
| **Core** | `core/` + `--core-only` | Default for real projects |
| **Pro** | this full repo | Long waves, full FM library, v5 protocols |

See [`core/README.md`](core/README.md).

### After generate — conductor

```bash
python3 conductor/conductor.py wake --project ./my-project
python3 conductor/conductor.py init-wave --project ./my-project -n 3
python3 conductor/conductor.py dispatch --project ./my-project --mode stub
bash ./my-project/orchestrator/scripts/preflight.sh ./my-project

make ship-check   # full product gate on the kit itself
```

---

## Features

<div align="center">

| 🔒 Safety | 🚀 Speed | 🧠 Intelligence |
|---|---|---|
| Route Sentinel (pre-execution blocking) | 11 archetypes = instant fit | Typed `PROJECT-INTENT.md` |
| VaultMMU (SHA-256 hash chain) | 5 core workflow templates | 18 failure modes with validators |
| OAP Security (deterministic policies) | Slash commands with cost caps | Self-improvement protocol (GEPA + Hermes) |
| 18 executable validators | Parallel conductor pattern | Living-folder memory bank |
| 7-layer verification stack | Engine-driven project generation | v5.0 self-monitoring & evolution layer |

</div>

### Progressive Disclosure — The Actual Fix for "Agent Forgets Everything"

A single giant markdown bloats the context window. Agents read it once, then forget the middle, then contradict it.

**Adaptoid OS uses progressive disclosure:**
- **Kernel** (~2K tokens) — loaded every session
- **Protocols** — loaded on trigger
- **Failure Modes** — loaded when symptom appears
- **Ecosystem** — pulled like books from a shelf, then closed

---

## Why Adaptoid OS Wins

Adaptoid OS is not a replacement for the frameworks below. It is a harness layer you can use with or without them.

| Dimension | LangGraph | CrewAI | AutoGen | **Adaptoid OS** |
|---|---|---|---|---|
| **Primary focus** | Stateful graphs | Role-based crews | Conversational agents | **Control stack / harness** |
| **Framework agnostic** | LangChain ecosystem | CrewAI | Microsoft ecosystem | ✅ **Sovereign core + optional bridges** |
| **Typed intent capture** | Manual | Manual | Manual | ✅ **`PROJECT-INTENT.md` + JSON Schema** |
| **Failure-mode library** | — | — | — | ✅ **18 FMs + validators** |
| **Deterministic safety layer** | Checkpoints | — | — | ✅ **Route Sentinel + VaultMMU + OAP** |
| **Living-folder memory** | In-graph | In-crew | In-chat | ✅ **Markdown + SQLite + Obsidian-ready** |
| **Self-validation** | — | — | — | ✅ **dogfood + preflight validators** |
| **Self-monitoring / consciousness** | — | — | — | ✅ **Consciousness Core protocol** |
| **Proactive assistant mode** | — | — | — | ✅ **Proactive Assistant protocol** |
| **Self-improving evolution** | — | — | — | ✅ **Evolution Engine protocol** |

**LangGraph** is excellent for durable, resumable graphs. Use Adaptoid's `claw_bridge/langgraph_adapter.py` when you want to export a plan to LangGraph.

**CrewAI** is great for quick role-based demos. Use the `crewai_adapter.py` when that model fits.

**AutoGen** shines for conversational multi-agent debate. Use the `autogen_adapter.py` for those waves.

**Adaptoid OS** focuses on the layer those frameworks do not: a failure-mode-aware control stack that stays independent.

---

## v5.0 Protocol Layer

The **v5.0 protocol layer** adds self-monitoring, durable memory-identity, safe evolution, proactive assistance, and workflow patterns on top of the v4.0 kernel. It is a protocol layer, not a franchise claim.

| Protocol | One-liner |
|---|---|
| [Consciousness Core](protocols/super-adaptoid/consciousness-core.md) | Self-monitoring, runtime introspection, and honest status reporting. |
| [Memory-Identity](protocols/super-adaptoid/memory-identity.md) | Persistent agent identity, session continuity, and memory-integrity rituals. |
| [Evolution Engine](protocols/super-adaptoid/evolution-engine.md) | Experimental prompt, skill, and workflow evolution with falsification gates. |
| [Proactive Assistant](protocols/super-adaptoid/proactive-assistant.md) | Proactive assistant mode: anticipate, surface, escalate, never interrupt. |
| [Hidden Gems](protocols/super-adaptoid/hidden-gems.md) | Discover, evaluate, and integrate lesser-known tools and patterns. |
| [Fable 5 Workflows](protocols/super-adaptoid/fable-5-workflows.md) | The v5.0 workflow library for long-horizon, multi-agent, and self-improving tasks. |
| [Super-Prompt](protocols/super-adaptoid/super-prompt.md) | Meta-prompt system for composing, versioning, and testing system prompts. |

See [`protocols/super-adaptoid/README.md`](protocols/super-adaptoid/README.md) for the full layer overview.

---

## Architecture

```
┌─────────────────────────────────────┐
│  Layer 3: v5.0 Protocols            │
│  consciousness · memory · evolution │
├─────────────────────────────────────┤
│  Layer 2: Public Product            │
│  README · docs/launch · ecosystem   │
├─────────────────────────────────────┤
│  Layer 1: Adaptoid Kernel (v4.0)    │
│  principles · protocols · validators│
└─────────────────────────────────────┘
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
├── ROADMAP.md
│
├── core/                        ← Core kit (portable minimum harness)
│   ├── README.md · MANIFEST.yaml
│   ├── hosts/                      host adapter templates
│   └── templates/                  HANDOFF + INDEX for generated projects
│
├── kernel/                      ← ALWAYS loaded (~2K tokens)
│   ├── PRINCIPLES.md               12 non-negotiable laws
│   ├── TWO-TIER.md                 Brain/Hands/Session
│   └── ANTI-HALLUCINATION.md       drift prevention
│
├── adaptor/
│   ├── engine.py                   brief → project + --host emit
│   └── host_emit.py                AGENTS/CLAUDE/Cursor/Codex/Grok
├── conductor/                   ← thin wake / dispatch / handoff runtime
├── benchmarks/                  ← speed + correctness suite
├── calibration/                 ← 50 harness cases
│
├── philosophy/                  ← the Three Pillars
├── patterns/                    ← extracted best practices
├── failure-modes/               ← 18 real failures + prevention
├── protocols/                   ← load on trigger (+ super-adaptoid/)
├── archetypes/                  ← 11 adaptation profiles
├── workflows/                   ← 5 core + domain YAML
├── slash-commands/              ← named orchestrator API
├── memory-bank/                 ← living folder memory
├── validators/                  ← 20+ executable scripts
├── templates/                   ← project skeleton
├── docs/launch/                 ← positioning + growth playbook
├── reference/                   ← OS_SETUP lite + ecosystem library
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

*A design-first harness built from real project post-mortems, research synthesis, and ecosystem gap analysis. Every claim links to a validator or ADR.*

</div>
