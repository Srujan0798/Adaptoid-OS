# Ecosystem — People (whose discipline to inherit)

> The practitioners whose patterns are baked into OS-Setup. Read the person when you want the WHY behind a rule.

| Person | Role | What to take | Where |
|---|---|---|---|
| **Andrej Karpathy** | ex-Tesla/OpenAI | CLAUDE.md discipline: think-before-coding · simplicity-first (200→50 lines) · surgical changes · goal-driven (tests first, loop). The kernel's build laws. | his CLAUDE.md / talks (corpus) |
| **Boris Cherny** | Claude Code lead, Anthropic | "give the agent a way to verify"; CLAUDE.md SHORT; explore→plan→code; sub-agents for investigation; hooks for determinism; Claude Code is a Unix utility. The kernel's truth + verification laws. | Latent.Space interview, code.claude.com best-practices (corpus) |
| **Simon Willison** | indie, llm/datasette | human-in-the-loop; context plumbing; TODO+reinforcement loops; "11 agents" is hype; the lethal trifecta (prompt-injection + exfil + sandboxing). The blast-radius + skepticism. | simonwillison.net (corpus) |
| **Anthropic engineering** | the lab | Building Effective Agents (5 patterns); Demystifying Evals (pass@k/pass^k); Brain/Hands/Session; auto mode; containment/blast-radius. The protocols. | anthropic.com/engineering (corpus + Q1/Q2-2026 posts) |
| **Matt Pocock** | TS educator | atomic skills (diagnose/triage/tdd/to-prd/to-issues/zoom-out/handoff/caveman); the skill quality bar. The skills-catalog. | mattpocock/skills (corpus) |
| **ruvnet** | multi-agent | swarm orchestration, HNSW memory, plugin ecosystems (Ruflo) — where enterprise multi-agent is heading. | github/ruvnet (corpus) |
| **Garry Tan / YC** | YC president | what early-stage AI startups actually ship; MVP discipline; instrument-to-learn; ICP/GTM. The startup-mvp archetype. | YC Lightcone / blog (corpus) |
| **GitHub / spec-kit team** | the platform | spec-driven development (constitution → specify → plan → tasks → implement). The .specify/ layer. | github/spec-kit (corpus) |

## The synthesis
OS-Setup is not one person's method — it's the intersection of:
- Karpathy's *restraint* (build less, verify more)
- Boris's *evidence* (never trust a claim; short contracts; verification primitives)
- Anthropic's *architecture* (Brain/Hands/Session; 5 patterns; evals)
- Willison's *caution* (humans in the loop; blast radius; no hype)
- Pocock's *atoms* (small composable skills)
- spec-kit's *contracts* (executable specs as truth)
- + your own *scars* (the 14 failure modes, observed live)

That last line is the unique part. Nobody else's setup is built from YOUR specific failures with executable validators that catch them. That's the edge.

`verified: 2026-05 (corpus across this project's research)`
