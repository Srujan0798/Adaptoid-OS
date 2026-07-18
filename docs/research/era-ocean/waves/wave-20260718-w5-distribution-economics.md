# Wave W5 — Distribution Economics: how the 2026 winners actually won

**Wave id:** `wave-20260718-w5-distribution-economics`
**Date:** 2026-07-18
**Scope:** Traction mechanics of the top agentic repos/frameworks — install moments, channels, directories, and the security cost of distribution. Verified star counts and adoption data as of 2026-07-18.
**Mode:** Live web research synthesis (8 searches, multi-source). One slice of an ocean — **not** complete coverage.

> **Honesty contract:** Star counts and stats below are from public secondary sources on the search date; they decay fast. This wave answers one question — *why do some harness products get adopted and others don't* — not the full growth literature.

---

## Executive thesis

**Content does not create traction. A 60-second install moment inside an existing channel does.**

Every breakout of 2025–2026 shares three properties:

1. **One-command install** where the user already lives (`npx …`, plugin marketplace, paste-a-file).
2. **A channel that ships discovery for free** (Claude Code plugin list, ClawHub, skills.sh, GitHub topic pages, awesome-lists).
3. **One shareable proof artifact** (a demo that a stranger can reproduce in minutes).

Nobody at the top won by having the most content. The largest corpora (aggregator lists) are *indexes pointing at* products, not products.

---

## Traction table (verified 2026-07-18)

| Project | Stars | Category | The install moment | The channel |
|---|---|---|---|---|
| OpenClaw | ~382k (0→346k in <5 months; passed React) | Channel daemon / personal agent | Self-host install | WhatsApp/Slack/Telegram etc. + ClawHub (44k skills) |
| Superpowers | ~243k | Claude Code workflow framework | Plugin install | Claude Code plugin ecosystem; SDLC skill chain |
| everything-claude-code | ~141k | Aggregator index | n/a (list) | GitHub search gravity |
| BMAD-METHOD | ~49k | Agile methodology harness (closest Adaptoid competitor) | `npx bmad-method install` | npm + 12 agent personas + Web Bundles → Gemini Gems / custom GPTs |
| awesome-claude-code | ~36.8k | Curated list | n/a | Canonical hand-curated list |
| GitHub Spec Kit | high, GitHub-official | Spec-driven development toolkit | `specify` CLI | GitHub brand + 30+ agent integrations |
| AGENTS.md standard | 60k+ repos using | Standard | Drop a file | AAIF / Linux Foundation stewardship |
| skills.sh (Vercel) | directory | Skill discovery | one-line skill install | Search by category/author/install count |

**BMAD is the one to study, not envy:** same "process discipline for agent dev" category as Adaptoid, ~49k stars — earned via npm one-liner, named personas people can retell ("the PM agent"), and packaging into surfaces non-devs already use (Gems/GPTs). Its content is *heavier* than Adaptoid's; its install is *lighter*. That asymmetry is the whole lesson.

---

## The dark side: distribution without gates

- ClawHub flagged **800+ malicious skills**; OpenClaw had **9 CVEs in 4 days** (one 9.9/10).
- MCP ecosystem: ~10–20k public servers indexed, but only **12.9% score "high trust"**; 41% of surveyed orgs run MCP in production anyway.
- → Marketplace-scale distribution is FM-20 at ecosystem scale. Adaptoid's deny-by-default / OAP stance is **validated by the leader's wounds**. Distribution push must never relax it.

## Eval reality check (feeds FM-21)

| Signal | Number (mid-2026) |
|---|---|
| SWE-bench Verified top agents | 74–78% (saturating) |
| Claude Mythos Preview on SWE-bench V | 93.9% — but ~19.8% of "solved" semantically wrong |
| Terminal-Bench top | 52–58% |
| **Real-world PR acceptance by human reviewers** | **35–50%** |

Benchmark-green ≠ reviewer-accepted. This is Adaptoid's founding "false done" thesis with industry numbers attached → distilled as **FM-21 eval theater**.

## MCP status delta

2026-07-28 RC: stateless core, Extensions, Tasks, MCP Apps, authorization hardening, formal deprecation policy. Donated to AAIF (Linux Foundation) Dec 2025. Registry in preview; namespace verification early. Keep dual-stack readiness note from W4-C; nothing new to adopt on hot path.

---

## Adaptoid delta — adopt / watch / refuse

| Move | Verdict | Why |
|---|---|---|
| `pip`/`uvx` one-liner install for engine | **Adopt** | The single highest-leverage gap vs BMAD |
| Claude Code plugin packaging (kernel + emitted skills) | **Adopt** | Channel with built-in discovery; Superpowers proof |
| List skills on skills.sh / agentskills.io | **Adopt** | Free discovery; skills already emitted since v5.3 |
| PRs to awesome-claude-code / awesome-harness-engineering / awesome-ai-agents lists | **Adopt** | Cheap, durable inbound; needs honest gates green first |
| One public demo repo w/ evidence trail as proof artifact | **Adopt** | Every winner has one reproducible wow |
| Named personas (BMAD-style) | **Watch** | Retellability is real; conflicts with lean two-tier — study only |
| Web Bundles → Gems / custom GPTs | **Watch** | Only after core channels prove demand |
| Skills marketplace as product | **Refuse** | Hot-path law; ClawHub's 800 malicious skills is the cautionary tale |
| Star-count growth hacks / celebrity angle | **Refuse** | Decays; evidence culture is the brand |

## Sources

- https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software/
- https://thenewstack.io/openclaw-github-stars-security/
- https://www.scriptbyai.com/claude-code-resource-list/
- https://github.com/bmad-code-org/bmad-method
- https://github.com/github/spec-kit
- https://codersera.com/blog/agents-md-complete-guide-2026/
- https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://github.com/ai-boost/awesome-harness-engineering
- https://agitech.group/blog/swe-bench-not-enough-ai-coding-agent-evaluation-2026
- https://presenc.ai/research/coding-agent-benchmarks-2026
- https://www.appliedtechnologyindex.com/research/2026-comparative-analysis-coding-agent-evaluation-harnesses-after-swe-bench/

**Ocean still open. Distribution literature barely sampled — growth loops, DevRel, docs-as-marketing all untouched.**
