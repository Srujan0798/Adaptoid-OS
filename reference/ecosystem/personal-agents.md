# Ecosystem — Personal / Multi-Channel Agents

> Pull ONLY if the project IS a personal assistant / multi-channel companion. For normal software projects, skip — this is a distinct product class.

| Tool | What | Pick when | Source |
|---|---|---|---|
| **OpenClaw** | personal AI across WhatsApp/Telegram/Slack/Discord/Signal/iMessage (20+ channels); local-first; gateway architecture; 196k★ | build a personal assistant reachable from chat apps | github/openclaw (corpus) |
| **Hermes** (Nous Research) | self-improving skills + dialectic user-modeling (Honcho) + cross-session FTS search; "grows with you" | assistant that learns the user over time | github (corpus) |
| **hermes-desktop** | ⚡ desktop companion for the Hermes framework — trending this month | desktop front-end for Hermes | github ⚡ |
| **nanobot** | ultra-light personal agent across terminal/Telegram/Discord/Slack/WeChat; MCP + skills | minimal multi-channel bot | nanobot.wiki (corpus) |

## Patterns these establish
- **Channel adapters** — one brain, many front-doors (chat apps, desktop, CLI). Decouple the agent from the channel.
- **User modeling** — Honcho-style dialectic memory of the person, not just the conversation.
- **Local-first** — privacy + ownership; the agent runs on the user's machine, data stays.
- **Self-improvement loop** — the agent edits its own skills as it learns (Hermes). The eternal-learning pattern.

## How OS-Setup uses this
- `startup-mvp`/`saas-product` building a personal-assistant product pull this file.
- The "self-improving skills" idea feeds OS-Setup's own `self-evolve` skill + the HALL_OF_SHAME → new-FM loop (the system learns from scars).
- Multi-channel = the Brain/Hands/Session split with channel adapters as additional "hands."

`verified: 2026-05 (hermes-desktop ⚡; OpenClaw/Hermes/nanobot corpus)`
