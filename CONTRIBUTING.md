# Contributing to Adaptoid OS

Thank you for helping make agentic AI more reliable. Every contribution compounds.

## Product filter (read first)

Before adding code or docs, answer yes to at least one:

1. Helps an agent **finish a project** on a host we don't control?  
2. Prevents a known **failure mode** with an executable check?  
3. Can a stranger use it in **under 10 minutes**?

If no to all three → put it in a discussion, not a PR. Prefer Core improvements over new protocols.

## How to Contribute

### 1. Report a Failure Mode
- Create `failure-modes/FM-NN-<name>.md` (existing format)
- Create `validators/<name>.sh`
- Wire into `preflight.sh` or document the trigger
- Add to `INDEX.md` and `failure-modes/README.md`
- `make ship-check` must pass

### 2. Add a host adapter
- Extend `adaptor/host_emit.py` + `core/hosts/`
- Add host to `core/MANIFEST.yaml` and tests in `tests/test_host_emit.py`

### 3. Add an Archetype
- Copy `archetypes/_TEMPLATE.md` → `<type>.md`
- Add signals in `adaptor/engine.py` if auto-detect should work
- Document in `INDEX.md`

### 4. Improve Conductor / Engine
- Keep Core path offline and dependency-free (stdlib + bash)
- Evidence in reports; HANDOFF is replace-not-append

### 5. Documentation
- Progressive disclosure: don't bloat `kernel/`
- Every new always-load path needs an `INDEX.md` entry
- Evidence beats speculation

## Development Setup

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd Adaptoid-OS
make ship-check   # full product gate — must pass
```

Faster loop:

```bash
bash validators/dogfood.sh
python3 tests/test_host_emit.py
bash benchmarks/run_bench.sh
```

## Pull Request Checklist
- [ ] `make ship-check` passes (or document why a subset ran)
- [ ] New files referenced from `INDEX.md` if user-facing
- [ ] No secrets / `.env` committed
- [ ] Evidence for any new FM claim
- [ ] Kernel still progressive-disclosure friendly

## Code of Conduct
Be kind, be evidence-driven, be honest about status. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
