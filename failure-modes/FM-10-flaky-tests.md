# FM-10 — Flaky Tests (pass alone, fail in suite)

**Symptom.** A test passes when run by itself but fails in the full suite, or fails intermittently. The agent re-runs until green and calls it done.

**Real incident.** DRO-FairML: `test_naive_fair_enforces_fairness` failed in the full run, passed in isolation — training-dependent randomness. The temptation was to "re-run until green," which hides real nondeterminism.

**Root cause.** Two mechanisms:
1. **Shared state** between tests (DB rows, global seed, files, module-level singletons) leaking across tests.
2. **Uncontrolled randomness** (unseeded RNG, time-dependent logic, order-dependent assertions).

**Blast.** False green hides a real bug; or false red wastes time; trust in the suite erodes; "re-run until green" becomes a habit that masks regressions.

**Prevention rule.**
- Each test starts from a clean state (fresh DB transaction rolled back, fresh tmp dir, re-seeded RNG).
- No module-level mutable singletons shared across tests.
- Seed all RNG in a fixture; assert on tolerances, not exact floats.
- A test that's flaky is QUARANTINED (marked, tracked) and FIXED within the wave — never ignored, never "re-run until green."

**Validator.** `validators/check_tests.sh`:
- Runs the suite twice with different `--randomly-seed` and in random order (`pytest-randomly`); fails if results differ.
- Greps for `time.time()`/`datetime.now()`/unseeded `random`/`np.random` in test paths.
- Flags `@pytest.mark.flaky`/quarantined tests older than one wave.

**Wire-in.** CI runs the suite twice (ordered + shuffled). Review protocol checks for quarantine debt.

**Fix when it fires.** Find the shared state or unseeded RNG; isolate it; don't paper over with retries.
