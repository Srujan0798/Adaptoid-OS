# Contributing to Adaptoid OS

Thank you for helping make agentic AI more reliable! Every contribution compounds.

## How to Contribute

### 1. Report a Failure Mode
Found a new way agentic runs fail? Add it:
- Create `failure-modes/FM-NN-<name>.md` following the existing format
- Create `validators/<name>.sh` to prevent it
- Add it to `INDEX.md` and `failure-modes/README.md`
- Run `bash validators/dogfood.sh` — it must pass

### 2. Add an Archetype
Missing your project type? Add it:
- Copy `archetypes/_TEMPLATE.md` to `<your-type>.md`
- Define tier defaults, high-risk FMs, deliverables
- Add to `INDEX.md`

### 3. Add a Domain Workflow
- Create `reference/workflows/<domain>.md`
- Include phases, agents, verification, timebox

### 4. Improve a Validator
- All validators support `--fix` and `--dry-run`
- Keep them focused: one responsibility per script
- Test on OS-Setup itself before submitting

### 5. Documentation
- Progressive disclosure is sacred. Don't bloat the kernel.
- Every new file needs an entry in `INDEX.md`.
- Use evidence: "this happened on project X" beats "this might happen."

## Development Setup

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd adaptoid-os
bash validators/dogfood.sh   # must pass
bash validators/preflight.sh # must pass
```

## Pull Request Checklist
- [ ] `dogfood.sh` passes
- [ ] `preflight.sh` passes
- [ ] New files added to `INDEX.md`
- [ ] No `.env` or secrets committed
- [ ] Evidence provided for any new FM claim

## Code of Conduct
Be kind, be evidence-driven, be honest about status. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
