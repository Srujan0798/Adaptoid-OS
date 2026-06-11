# Why I Built Adaptoid OS (and Why It Is Not Another Framework)

Agentic AI projects tend to fail in a small set of predictable ways.

## The Same Four Failures

Over and over, the same problems show up:

1. **State drift.** An agent crashes, restarts, and forgets what wave it was on.
2. **Wrong tool calls.** It invokes a tool that does not match the current state.
3. **Unverified "done" claims.** It reports completion but there is no evidence.
4. **Embarrassing artifacts.** Files that should never see production slip into commits.

These are not model failures. They are harness failures.

## Frameworks Give You Primitives, Not Guardrails

LangGraph, CrewAI, AutoGen, and the OpenAI Agents SDK are good at what they do. They give you nodes, roles, conversations, and handoffs. What they do not give you is a built-in answer to "how will this fail, and how will we catch it before production?"

That is the gap Adaptoid OS tries to close.

## What Adaptoid OS Actually Does

Adaptoid OS v4.0 is a harness, not a framework. Its job is to make the failure modes explicit and catch them early.

- **18 failure modes** (FM-01 State Drift → FM-18 Agent Escalation Bypass), each with a validator.
- **Typed project intent** via `PROJECT-INTENT.md` and JSON Schema.
- **Memory bank** with automated sync and event sourcing.
- **Wave transitions** enforced in workflow files.
- **One-command scaffolding** with `adaptor/engine.py`.
- **Optional framework adapters** for LangGraph, CrewAI, and AutoGen.

The core has zero external framework dependencies. The adapters are opt-in.

## How to Try It

```bash
curl -sSL https://raw.githubusercontent.com/Srujan0798/Adaptoid-OS/main/install.sh | bash
```

Or clone and run the validators:

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd Adaptoid-OS
bash validators/dogfood.sh
```

## What It Is Not

It is not polished. It is not a silver bullet. It is not trying to replace the frameworks you already use.

It is one developer's attempt to make agentic systems less fragile.

If you are shipping agentic systems in production, feedback is welcome.

**Repo:** [github.com/Srujan0798/Adaptoid-OS](https://github.com/Srujan0798/Adaptoid-OS)

---

*Feedback welcome via GitHub Issues.*
