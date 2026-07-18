# FM-21 — Eval theater (benchmark-green ≠ reviewer-accepted)

**Symptom.** "Done" is claimed from a green benchmark, test suite, or self-graded check, but the work fails human review, is semantically wrong, or breaks in real use. Confidence rises while quality doesn't.

**Real incident.** Industry-wide, mid-2026: top agents at 74–78% SWE-bench Verified (one claim at 93.9% with ~19.8% of "solved" cases semantically wrong) while real human PR acceptance sits at 35–50%. Locally: acceptance commands that were `true`/`echo` no-ops auto-passed conductor shell mode until v5.4 hardening.

**Root cause.** The success signal measures something cheaper than the actual goal: a public benchmark instead of your repo's conventions; a no-op acceptance instead of a failing-capable command; a self-grade instead of an external check (maker = checker).

**Blast.** Ship gate green on unshippable work — the most expensive form of FM-09 false status, because the evidence *looks* rigorous.

**Prevention.**
- Acceptance commands must be able to fail: no `true`, `:`, `exit 0`, bare `echo` (conductor rejects these in shell mode).
- Define done as **golden tasks in this project**, never a public leaderboard number.
- Maker ≠ checker: verification by a second agent, a human, or a mechanical end-state test the maker can't edit (do not delete/weaken tests to go green — that is this FM).
- Report the honest gap: if only proxy checks ran, say so in the report.

**Validator.** `conductor.py` shell-mode no-op rejection; `check_status_claims.sh`; `check_tests.sh`.

**Wire-in.** Conductor dispatch (always) · preflight · review protocol before merge.
