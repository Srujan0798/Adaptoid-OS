# Adaptoid OS v5.0 Demo Script

Use this script to record a 60-second demo GIF for the README and launch posts.

## Setup

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd Adaptoid-OS
```

## Scene 1: One-command validation (0-15s)

Type:

```bash
bash validators/dogfood.sh
```

Expected output:

```text
================ OS-SETUP DOGFOOD ================
...
OK  consciousness-core protocol valid
OK  memory-identity protocol valid
OK  evolution-engine protocol valid
OK  proactive-assistant protocol valid
OK  hidden-gems protocol valid (36 catalog entries)
OK  fable-5-workflows protocol valid (10 workflows)
OK  super-prompt protocol valid
OK  README passes 10-point heuristic
===================================================
DOGFOOD: PASS ✅  The kit is internally consistent.
```

## Scene 2: Typed project intent (15-30s)

Show `PROJECT-INTENT.md` structure and run:

```bash
bash validators/check_intent.sh
```

Expected output:

```text
OK check-intent: PROJECT-INTENT.md valid
```

## Scene 3: Super-Adaptoid protocols (30-45s)

List the protocols:

```bash
ls protocols/super-adaptoid/
cat protocols/super-adaptoid/consciousness-core.md | head -n 20
```

## Scene 4: Worked example (45-60s)

```bash
cd examples/super-adaptoid
ls
cat PROJECT-INTENT.md | head -n 10
```

## Recording tools

Recommended:
- [asciinema](https://asciinema.org/) + [agg](https://github.com/asciinema/agg) for terminal GIFs
- [terminalizer](https://github.com/faressoft/terminalizer) for styled recordings
- [Screen Studio](https://www.screen.studio/) (macOS) for polished captures

Save the final GIF as `docs/demo.gif` and reference it in `README.md`.
