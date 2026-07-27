#!/usr/bin/env bash
# Runs all wired validators. Green required before merge/ship.
# Usage: preflight.sh [project_root] [--fix] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"
HERE="$(cd "$(dirname "$0")" && pwd)"
rc=0

# Parse --fix and --dry-run (pass through to all validators)
EXTRA_ARGS=()
for arg in "$@"; do
  case "$arg" in
    --fix|--dry-run) EXTRA_ARGS+=("$arg") ;;
  esac
done

run() {  # run <script> <args...>
  local name="$1"; shift
  if [ -x "$HERE/$name" ] || [ -f "$HERE/$name" ]; then
    echo "── $name ──"
    if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
      bash "$HERE/$name" "$@" "${EXTRA_ARGS[@]}" || rc=1
    else
      bash "$HERE/$name" "$@" || rc=1
    fi
    echo ""
  fi
}

echo "================ OS-Setup PREFLIGHT ================"
run validate_state.sh "$ROOT"
run check_references.sh "$ROOT"
run context_budget.sh "$ROOT"
run publish_gate.sh "$ROOT"
run check_silent_failures.sh "$ROOT"
[ -d "$ROOT/configs" ] && run check_config.sh "$ROOT"
[ -f "$ROOT/results/metrics.json" ] && run check_metrics.sh "$ROOT"
# FM-02 only if marker provided or src/ exists
MARKER="$(basename "$(cd "$ROOT" 2>/dev/null && pwd)")"
[ -d "$ROOT/src" ] && [ "$MARKER" != "." ] && run check_processes.sh "$MARKER"
[ -f "$ROOT/HANDOFF.md" ] && run check_handoff.sh "$ROOT"
[ -d "$ROOT/work/reports" ] && run check_status_claims.sh "$ROOT"
run check_entailment.sh "$ROOT"
[ -d "$ROOT/work" ] && run check_parallel_writes.sh "$ROOT"
[ -f "$ROOT/adaptoid.config.yaml" ] && run check_cost_ceiling.sh "$ROOT"
( [ -d "$ROOT/tests" ] || [ -d "$ROOT/test" ] || find "$ROOT" -maxdepth 2 \( -name 'test_*.py' -o -name '*_test.py' \) 2>/dev/null | grep -q . ) && run check_tests.sh "$ROOT"
( [ -f "$ROOT/HIERARCHY.md" ] || [ -f "$ROOT/docs/SCOPE_GUARD.md" ] ) && run check_scope.sh "$ROOT"
[ -f "$ROOT/adaptoid.config.yaml" ] && run route_sentinel.sh "$ROOT"
[ -d "$ROOT/policies" ] && run oap_security.sh "$ROOT"
[ -f "$ROOT/PROJECT-INTENT.md" ] && run check_intent.sh "$ROOT"
[ -f "$ROOT/orchestrator/memory/session/events.jsonl" ] && run audit_chain.sh "$ROOT"
echo "==================================================="
if [ "$rc" -eq 0 ]; then echo "PREFLIGHT: PASS ✅"; else echo "PREFLIGHT: FAIL ❌ (fix above before merge/ship)"; fi
exit $rc
