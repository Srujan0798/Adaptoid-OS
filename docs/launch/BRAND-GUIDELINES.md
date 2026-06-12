# Adaptoid OS Brand Guidelines

## Name

### Primary name

**Adaptoid OS**

The full product name is "Adaptoid OS." The "OS" suffix clarifies that this is an operating system layer for agentic AI, not a model or a chat interface.

### Internal-only names

- **Super-Adaptoid** — a protocol layer name (`protocols/super-adaptoid/`), not a product or franchise claim. Use only in technical documentation and only to refer to the v5.0 protocol suite.
- **Proactive Assistant** — the neutral feature name for proactive assistant mode. Avoid "Jarvis" or "J.A.R.V.I.S." to prevent franchise confusion.

## Name Analysis

### Trademark and conflict scan

- **"Adaptoid"** is a recognized Marvel Comics character / android concept ("Super-Adaptoid" appears in Marvel comics and related media).
- **Risk level**: moderate. "Adaptoid" alone is distinctive enough in the agentic-AI context that it is unlikely to be confused with a comic-book villain, but Marvel/Disney are active IP enforcers.
- **Mitigation**: always pair "Adaptoid" with "OS" in public-facing material ("Adaptoid OS"). Never use "Super-Adaptoid" as a standalone product name, slogan, or marketing term. Keep "Super-Adaptoid" references inside `protocols/super-adaptoid/` and technical docs.
- **No Marvel language**: do not use words like "superhero," "supervillain," "Avengers," "franchise," or origin-story metaphors in the README, launch docs, or public posts.
- **No character likeness**: do not use comic-style imagery, shields, masks, or character silhouettes in logos or social previews.

### Domain and search considerations

- Search "Adaptoid OS" returns this project and a small set of unrelated results. Good differentiation.
- Search "Adaptoid" alone returns Marvel-related content. Always use the full "Adaptoid OS" form in URLs, titles, and tags.

## Tagline Options

Use the primary tagline in most contexts. Rotate alternatives only when the primary feels repetitive.

1. **Primary**: *Adapt. Validate at runtime. Verify relentlessly. Compound carefully.*
2. *The Agent Operating System for Agentic AI.*
3. *A harness-first OS that prevents the 18 ways agentic AI fails.*
4. *Framework-agnostic. Failure-mode-aware. Self-improving.*
5. *Turn any LLM into a verified agentic workforce.*

## README Blueprint

The README must answer these questions in order:

1. **What is it?** — one-sentence description above the fold.
2. **Why should I care?** — the 18 failure modes problem paragraph.
3. **How is it different?** — comparison matrix with LangGraph, CrewAI, AutoGen.
4. **What do I get?** — Super-Adaptoid layer + features matrix.
5. **How do I try it?** — Quick Start (3 options).
6. **How is it built?** — architecture diagram + folder map.
7. **How do I help?** — Contributing + License.

## Voice and Tone

- **Honest, not hype.** Every claim must be tied to a validator, example, or ADR.
- **Engineering-first.** Use precise terms: harness, control stack, validator, protocol, failure mode.
- **Friendly but restrained.** Avoid exclamation points, all-caps, and urgency language.
- **Specific over generic.** "Pre-execution wrong-route blocking" beats "enterprise-grade safety."

## Visual Identity

### Color palette

| Role | Suggested color | Notes |
|---|---|---|
| Primary accent | `#0A84FF` (blue) | trustworthy, technical |
| Safety / pass | `#30D158` (green) | dogfood, preflight passing |
| Warning | `#FF9F0A` (orange) | archetypes, attention |
| Failure / stop | `#FF453A` (red) | failure modes, blocking |
| Neutral text | `#F5F5F7` on dark, `#1D1D1F` on light | accessible contrast |

### Badges

Use shields.io badges exactly as in README.md:

- Dogfood
- Preflight
- Version
- License
- Archetypes
- Failure Modes

### Imagery

- Prefer diagrams, ASCII architecture, and code snippets over illustrations.
- Demo GIF should show a real terminal session, not animated characters.
- Social preview should be text-forward: project name, tagline, and one proof point.

## Terminology Dictionary

| Use this | Not this |
|---|---|
| Adaptoid OS | Adaptoid (alone) |
| Super-Adaptoid layer / protocols | Super-Adaptoid product, Super-Adaptoid franchise |
| Proactive Assistant | Jarvis, J.A.R.V.I.S., any fictional AI assistant name |
| Agent Operating System | AI Operating System (too generic) |
| Harness | Wrapper |
| Failure mode | Bug type |
| Validator | Check |
| Protocol | Rule |
| Progressive disclosure | Context management |

## Brand Consistency Checklist

Before publishing any public material, confirm:

- [ ] "Adaptoid OS" appears at least once in the title or first paragraph.
- [ ] "Super-Adaptoid" is only used as a protocol layer name.
- [ ] No Marvel, Disney, or superhero language appears.
- [ ] Every strong claim has evidence, a validator, or a citation.
- [ ] Tone is honest, engineering-first, and free of hype.
- [ ] Badges match README style.
- [ ] Visuals are diagram/code-centric, not character-centric.
- [ ] License (MIT) and contribution path are mentioned or linked.

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Marvel/Disney trademark challenge | Low | High | Use "Adaptoid OS" not "Adaptoid"; keep "Super-Adaptoid" internal/technical only. |
| Generic confusion with other "AI OS" projects | Medium | Medium | Own the "Agent Operating System" phrase with specific failure-mode differentiation. |
| Hype backlash | Medium | Medium | Evidence-required claims; dogfood/preflight badges; public ADRs. |
