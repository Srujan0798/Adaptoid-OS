# Ecosystem — Skills Catalog (the 1000+ skill universe)

> Skills are the portable capability unit (agentskills.io). 3,200+ repos tagged `claude-skills`; `awesome-agent-skills` lists 1000+. You don't write most skills — you PULL them. This maps the taxonomy + sources.

## Where to get skills
| Source | What | Note |
|---|---|---|
| **agentskills.io** | the standard + registry | install into any compatible tool |
| **mattpocock/skills** | the canonical atomic-skill set | the reference quality bar |
| **Skills/** (local, on this Desktop) | engineering/productivity/finance/legal/marketing/sales/product-management/data/design | already on your machine — reuse it |
| **knowledge-work-plugins** | ⚡ open plugins for knowledge workers in Claude | trending this month |
| **github topic: claude-skills** | 3,200+ repos | search by domain |
| **awesome-agent-skills** | 1000+ curated | discovery hub |

## The atomic-skill taxonomy (mattpocock-validated patterns)
Engineering: `tdd` · `code-review` · `diagnose` · `triage` · `debug` · `architecture` · `system-design` · `tech-debt` · `deploy-checklist` · `incident-response`
Planning: `to-prd` · `to-issues` · `zoom-out` · `prototype` · `spec-panel` · `brainstorm`
Productivity: `task-management` · `memory-management` · `standup` · `handoff` · `update-command`
Compression/meta: `caveman` (~75% token cut) · `find-skills` · `prompt-master`
Output: `humanizer` · `fact-checker` · `front-end-slides` · `decision-toolkit`
Infra: `mcp-builder` · `docker-compose` · `github-actions` · `pre-commit`
Domain (examples): `pdf-processing` · `excel-processing` · `web-scraping` · `api-design` · `sqlalchemy-orm` · `alembic-migrations` · `react-hooks` · `tanstack-query`

## Two kinds of skills in OS-Setup projects (don't confuse them — this caused real confusion)
1. **Orchestrator skills** (`orchestrator/skills/`) — YOURS, for planning/dispatch/review (write-task-file, plan-wave, review-report...). Workers can't see these.
2. **Worker skills** — the worker's OWN library (agentskills.io, their CLI's `skills.sh`, Claude built-ins). Task briefs list these BY NAME so the worker installs/looks them up.

## How OS-Setup uses this
- At setup, for the detected archetype, it lists the worker skills tasks will likely need (e.g., nlp-pipeline → `pdf-processing`, `excel-processing`; saas → `api-design`, `react-hooks`).
- It pins them in `skills.manifest.json` + `skills-lock.json` (reproducibility — FM-06 cousin).
- It reuses your local `~/Desktop/Skills/` where relevant instead of reinventing.

## Build-your-own (rare)
Only write a skill when no existing one fits AND it's reused 3+ times. Format: `SKILL.md` per spec in `protocols/` / agentskills.io. Validate with `skills-ref validate`.

`verified: 2026-05 (knowledge-work-plugins ⚡; rest corpus + local Skills/ confirmed on disk)`
