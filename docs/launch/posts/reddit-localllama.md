# Reddit r/LocalLLaMA Launch Post

**Title:** Adaptoid OS v5.0 — an agent operating system for local LLMs with runtime validators

**Body:**

Hey r/LocalLLaMA,

I’ve been running local LLMs for agentic tasks and kept hitting the same failures: agents call the wrong tool, forget state between sessions, claim success without evidence, or silently revert config changes. Existing frameworks give you graph nodes and crews, but not a runtime control layer.

So I built Adaptoid OS:

- Framework-agnostic harness (works with Ollama, vLLM, llama.cpp, etc.)
- 18 documented failure modes with matching bash validators
- Route Sentinel blocks wrong-route transitions before execution
- VaultMMU keeps memory integrity with hash chains
- v5.0 adds self-monitoring, durable memory-identity, evolution, and proactive-assistant protocols
- Progressive disclosure: kernel stays ~2K tokens, advanced protocols load on trigger

The validator-first design means every doc/protocol has a `bash validators/check_*.sh` script. `bash validators/dogfood.sh` must pass before claiming completion.

Repo: https://github.com/Srujan0798/Adaptoid-OS

Would love your thoughts on what safety checks are missing for local agent deployments.
