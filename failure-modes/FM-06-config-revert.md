# FM-06 — Config Revert (param silently changed back)

**Symptom.** You fixed a parameter, but a later run uses the old value. An editor, linter, autoformatter, or another agent silently reverted it. The run looks fine but is wrong.

**Real incident.** DRO-FairML: after fixing `epochs` 30→60 in the experiment runner, an external edit reverted Naive epochs back to 30. Caught only by re-reading the file and noticing; the wrong-param process had to be killed and restarted. The verified config (`epochs=60, K_inner=10`) drifted from what was actually running.

**Root cause.** Critical params lived inline in code/CLI where any edit could change them, with no assertion that the running value matched the intended one. "Wrong" and "right" were visually identical.

**Blast.** Hours of compute on invalid params; results that silently don't match the methodology; near-use of invalid results.

**Prevention rule.**
1. Critical params live in ONE config file (`configs/default.yaml`), not scattered inline.
2. The program READS them from config — never hardcodes.
3. At startup the program ASSERTS the critical values and PRINTS them, so a revert fails loud:
   ```python
   assert cfg.epochs == 60, f"epochs={cfg.epochs}, expected 60 — config drift!"
   print(f"[config] epochs={cfg.epochs} K_inner={cfg.k_inner} ... (asserted)")
   ```
4. The config file is covered by FM-05's single-source rule and by tests.

**Validator.** `validators/check_config.sh`:
- Diffs `configs/default.yaml` against a committed `configs/default.lock` of critical keys; fails on unexpected change without an ADR.
- Greps code for hardcoded values that should come from config (e.g., literal `epochs=30`).

**Wire-in.** Pre-commit + CI + every long-job startup assertion.

**Fix when it fires.** Restore the intended value, add/refresh the lock, add the startup assertion if missing.
