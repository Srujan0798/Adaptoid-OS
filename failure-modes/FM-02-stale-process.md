# FM-02 — Stale Process with Wrong Params

**Symptom.** A long-running job keeps consuming CPU; results trickle in but are subtly wrong; a "new" run seems to make no progress because an old one holds the cores.

**Real incident.** ⚡LIVE during this folder's build: `ps aux` showed PID 89078 — a DRO-FairML batch running **157 minutes** with `--k_inner 5`, while the project's verified-correct config is `K_inner=10`. Earlier in the same project's history, a process started with `epochs=30` ran for hours alongside a corrected `epochs=60` process, wasting a full evening of compute and producing invalid results that were nearly used.

**Root cause.** Two compounding errors:
1. A new run was launched without checking whether an old one was still alive.
2. Params were passed on the CLI, not asserted against the canonical config, so "wrong" looked identical to "right" until you read 150 chars of `ps` output.

**Blast.** Hours of wasted compute. Invalid results that look valid. Two processes corrupting the same output directory. The single most expensive recurring failure in this project history.

**Prevention rule.** Before launching any long job: (1) check for an existing one; (2) params come from the config file; (3) the program asserts critical params at startup and prints them.

**Validator.** `validators/check_processes.sh`:
- `ps aux | grep <project-marker>` → if a run is already alive, REFUSE to start a second and print the offender's PID + full command line.
- Greps the running command for params and compares to `configs/default.*`; warns loudly on mismatch.

**Wire-in.**
- `make run` / `make train` calls it first and aborts on conflict.
- Every long-job script starts with: read config → assert critical params → print them → register PID in `orchestrator/memory/states/running.json`.

**Fix when it fires.** `kill` the stale PID, delete its partial output, confirm the config, relaunch ONE process.
