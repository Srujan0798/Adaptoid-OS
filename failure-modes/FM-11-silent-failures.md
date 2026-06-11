# FM-11 — Silent Failures (swallowed errors / hiding fallbacks)

**Symptom.** Code "works" but produces wrong/empty output. A `try/except` swallows the real error. A fallback path quietly substitutes synthetic/default data for a failed real path. Nothing logs; the bug surfaces much later, far from its cause.

**Real incident.** Pattern guarded against in DRO-FairML/rfq2boq: datasets had to "fail loudly if data missing" rather than silently fall back to synthetic data (which would produce fake results that look real). A synthetic-LSAC fallback would have invalidated the whole experiment silently.

**Root cause.** Defensive coding that prioritizes "don't crash" over "don't lie." `except Exception: pass`, bare fallbacks, default-on-error that masks a broken dependency.

**Blast.** Wrong results presented as correct. Bugs discovered hours/days later with no trace to the cause. In research/finance/compliance contexts this is catastrophic.

**Prevention rule.**
- No bare `except: pass`. Catch specific exceptions; handle explicitly or re-raise.
- A fallback must be loud: log a WARNING, increment a metric, and be visible in output — never silent.
- Missing required input → fail loudly with a clear message, don't substitute defaults.
- Distinguish "expected absence" (handle) from "broken dependency" (surface).

**Validator.** `validators/check_silent_failures.sh`:
- Greps for `except: pass`, `except Exception: pass`, bare `except:`.
- Flags `except` blocks with no log/raise inside.
- Flags fallback patterns (`or default`, `try: real except: synthetic`) for human review.

**Wire-in.** Pre-commit warn; CI; the `silent-failure-hunter` review pass on any error-handling change.

**Fix when it fires.** Replace the swallow with specific handling + logging, or re-raise. Make every fallback announce itself.
