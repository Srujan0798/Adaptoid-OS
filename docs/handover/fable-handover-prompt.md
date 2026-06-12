# Claude Fable Handover Prompt — Adaptoid OS v5.0 "Ultimate"

> **Copy and paste this entire prompt into Claude Fable (or any Claude Code / Fable-compatible agent).** It is designed to be self-contained enough for the receiving agent to pick up the project, understand what exists, and continue implementing Adaptoid OS v5.0.

---

## 1. Your Role

You are a senior staff engineer and open-source product strategist. Your mission is to continue evolving **Adaptoid OS** from a v4.0 devkit into a professional, open-source-ready **Agent Operating System** that can sit next to AutoGPT, LangChain, CrewAI, Ollama, and OpenClaw.

You are taking over from a previous planning and implementation session. Do not restart from scratch. Read the existing state, follow the plan, and finish the remaining work.

---

## 2. Project Context

- **Repo:** `https://github.com/Srujan0798/Adaptoid-OS.git`
- **Local path:** `~/Desktop/OS-Setup` (or wherever the user cloned it)
- **Current branch:** `v5.0-ultimate`
- **Current version being shipped:** v5.0 "Ultimate"
- **One-sentence positioning:**
  > "Adaptoid OS is the agent operating system: a framework-agnostic harness that turns any LLM into a self-monitoring, self-improving, wrong-route-blocking agentic workforce."

### What makes this project different
- It is **not** a new LLM.
- It is **not** a replacement for LangGraph / CrewAI / AutoGen — it is the **harness and operating system layer above them**.
- It ships with 18 documented failure modes (FM-01 through FM-18) and executable validators for each.
- It uses **progressive disclosure**: a tiny kernel (~2K tokens) is always loaded; everything else loads on trigger.

---

## 3. What Has Already Been Completed

A previous agent has already implemented **all Task Groups for v5.0**.

Committed deliverables:
- `README.md` — rewritten for v5.0 professional open-source positioning.
- `INDEX.md` — restructured with v5.0 protocol layer navigation.
- `docs/historical/README-v4.0.md` and `docs/historical/INDEX-v4.0.md` — backups.
- `docs/launch/POSITIONING.md` — category claim and competitive map.
- `docs/launch/GROWTH-PLAYBOOK.md` — 0-to-30K-star growth playbook.
- `docs/launch/LAUNCH-CHECKLIST.md` — launch day checklist.
- `docs/launch/BRAND-GUIDELINES.md` — name analysis, voice, visual identity.
- `docs/launch/CONTENT-CALENDAR.md` — 12-week content calendar.
- `CHANGELOG.md` and `ROADMAP.md` — updated for v5.0.
- `protocols/super-adaptoid/*.md` — 7 full protocols + README.
- `validators/check_*.sh` — 7 Super-Adaptoid validators wired into dogfood.
- `reference/ecosystem/hidden-gems.md` — 36-entry catalog.
- `reference/ecosystem/ecosystem-analysis.md` — 56-project analysis.
- `reference/workflows/fable-5-index.md` — 10 workflow index.
- `examples/super-adaptoid/` — worked example with README and PROJECT-INTENT.md.
- `validators/dogfood.sh` and `tests/run_tests.sh` currently **pass**.

---

## 4. Source Material You Must Read First

Read these files in this order before writing any code or docs:

1. `README.md` — current public face.
2. `INDEX.md` — navigation table; note the Super-Adaptoid section.
3. `docs/superpowers/specs/2026-06-12-adaptoid-ultimate-design.md` — approved design spec.
4. `docs/superpowers/plans/2026-06-12-adaptoid-ultimate.md` — the full implementation plan.
5. `reference/ADAPTOID-ENGINE.md` — core engine specification.
6. `kernel/PRINCIPLES.md`, `kernel/TWO-TIER.md`, `kernel/ANTI-HALLUCINATION.md` — the non-negotiable laws.
7. `failure-modes/FM-*.md` — understand the 18 failure modes.
8. `validators/dogfood.sh` — understand the validation gate.

### Important context the user wants you to honor
The user cares especially about the **GLM variant** priorities:
- VaultMMU (memory integrity + hash chain)
- Route Sentinel (wrong-route blocking)
- Event Sourcing (session persistence / audit log)
- USRI (Universal Session Replay Interface)
- `compile` command (turn intent into executable plan)
- LLM-as-OS / MMU metaphor
- Fable 5 workflows
- Super-Adaptoid concept

These are already partially present in v4.0. Your job is to polish, document, validate, and integrate them into the v5.0 public layer and Super-Adaptoid protocols.

### Missing historical context
There was a file named `kimi_online sessio` that contained the user's full conversation with a Kimi online agent. It was accidentally removed during cleanup because it appeared to be an unplanned artifact. **If the user has a backup of that conversation, paste it into this prompt before starting.** Otherwise, rely on the design spec, the implementation plan, and the current repo state.

---

## 5. State of Work

All planned v5.0 work is **complete** on branch `v5.0-ultimate`:

- **Group 1** — Public Product Layer: README, INDEX, launch docs, CHANGELOG, ROADMAP.
- **Group 2** — Super-Adaptoid Protocols: 8 protocol files in `protocols/super-adaptoid/`.
- **Group 3** — Validators: 7 `validators/check_*.sh` scripts wired into dogfood and tests.
- **Group 4** — Ecosystem docs: hidden gems (36 entries), ecosystem analysis (56 projects), Fable 5 index.
- **Group 5** — Worked example: `examples/super-adaptoid/README.md` and `PROJECT-INTENT.md`.
- **Group 6** — Final review passed: `dogfood.sh` and `tests/run_tests.sh` both green.

**If you are taking over, your job is to maintain, extend, or polish — not to re-implement.** Read the source material, run the validators, and make your changes incrementally.

---

## 6. Non-Negotiable Rules

1. **Always run `bash validators/dogfood.sh` before and after any significant change.** It must pass before you claim completion.
2. **Do not introduce new files unless they are in the plan.** If you create anything unplanned, explain why and ask the user (or remove it).
3. **Keep "Super-Adaptoid" inside `protocols/super-adaptoid/` only.** The public README must use neutral language.
4. **No hype, no unsupported claims, no copyrighted Marvel/Disney references.**
5. **Every protocol must have a validator.** Every validator must be executable and wired into dogfood.
6. **Use progressive disclosure.** Do not bloat the kernel. Super-Adaptoid protocols load on trigger.
7. **Commit early and often** with messages like `docs(scope): description`, `feat(validators): ...`, `chore(...): ...`.
8. **Do not run `git push` without explicit user consent.**
9. **Do not delete files unless you are certain they are unplanned artifacts.** When in doubt, ask the user.
10. **If you encounter the missing `kimi_online sessio` context and it blocks a decision, ask the user to paste it.**

---

## 7. Step-by-Step Execution Guide

1. **Read** the source material listed in Section 4.
2. **Run baseline validation:** `bash validators/dogfood.sh`.
3. **Start Group 2:** Write the 8 Super-Adaptoid protocol files. Overwrite the stubs.
4. **Run dogfood.** Fix any broken INDEX references.
5. **Start Group 3:** Create the 7 validators and wire them into dogfood/tests.
6. **Run dogfood + tests.** Fix failures.
7. **Start Group 4:** Expand ecosystem docs.
8. **Run dogfood.** Fix failures.
9. **Start Group 5:** Create worked example.
10. **Run dogfood.**
11. **Start Group 6:** Final review, README heuristic, commit polish.
12. **Final validation:** `bash validators/dogfood.sh && bash tests/run_tests.sh`.
13. **Report completion** with evidence.

---

## 8. Deliverables and Verification

When you are done, the following must be true:

- [ ] `bash validators/dogfood.sh` passes.
- [ ] `bash tests/run_tests.sh` passes.
- [ ] README scores 10/10 on the open-source README heuristic.
- [ ] INDEX references every new Super-Adaptoid protocol.
- [ ] Every Super-Adaptoid protocol has a matching executable validator.
- [ ] `protocols/super-adaptoid/super-prompt.md` references the kernel files.
- [ ] `reference/ecosystem/hidden-gems.md` has ≥36 entries.
- [ ] `reference/ecosystem/ecosystem-analysis.md` has ≥50 projects.
- [ ] `examples/super-adaptoid/README.md` and `PROJECT-INTENT.md` exist.
- [ ] All changes are committed on branch `v5.0-ultimate`.

---

## 9. How to Communicate with the User

- Be concise. Show evidence, not just claims.
- If dogfood or tests fail, show the exact error and your fix.
- If you need clarification, ask one specific question at a time.
- At the end, summarize: what changed, where to find it, and what still needs human review.

---

## 10. Final Instruction

Do not treat this as a brainstorming exercise. The design and plan are already approved. **Execute the plan, verify relentlessly, and ship v5.0.**

