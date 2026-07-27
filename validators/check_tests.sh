#!/usr/bin/env bash
# FM-10 — Flaky tests (shared state / uncontrolled randomness).
# Usage: check_tests.sh [project_root] [--fix] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"
FIX=0
DRY=0
shift || true

for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    --dry-run) DRY=1 ;;
  esac
done

fail=0

# Find test files
TEST_DIRS=("$ROOT/tests" "$ROOT/test" "$ROOT/src" "$ROOT")
TEST_FILES=$(find "${TEST_DIRS[@]}" -maxdepth 3 \( -name 'test_*.py' -o -name '*_test.py' -o -name '*.test.js' -o -name '*.spec.js' -o -name '*.test.ts' -o -name '*.spec.ts' \) 2>/dev/null)

if [ -z "$TEST_FILES" ]; then
  echo "OK FM-10: no test files found"
  exit 0
fi

# Check for uncontrolled randomness / shared-state smells
while IFS= read -r f; do
  [ -z "$f" ] && continue
  # Unseeded RNG
  if grep -qE '\brandom\.(rand|randint|choice|shuffle|sample)\b|\bnp\.random\.(rand|randn|choice)\b' "$f" && ! grep -qE '\bseed\b|\bnp\.random\.seed\b|\brandom\.state\b' "$f"; then
    echo "WARN FM-10: $f uses unseeded randomness"
  fi
  # Time-dependent logic
  if grep -qE '\btime\.time\(\)\b|\bdatetime\.now\(\)\b|\bdatetime\.today\(\)\b' "$f"; then
    echo "WARN FM-10: $f uses time-dependent logic without mocking"
  fi
  # Module-level mutable singletons
  if grep -qE '^[A-Za-z_][A-Za-z0-9_]* *= *\{\s*$|^[A-Za-z_][A-Za-z0-9_]* *= *\[\s*$' "$f"; then
    echo "WARN FM-10: $f has module-level mutable structures (possible shared state)"
  fi
  # Stale quarantined tests
  quarantined=$(grep -HnE '@pytest\.mark\.flaky|@pytest\.mark\.skip\(.*flaky' "$f" 2>/dev/null)
  if [ -n "$quarantined" ]; then
    echo "WARN FM-10: $f contains quarantined/flaky tests:"
    echo "$quarantined" | sed 's/^/  /'
  fi
done <<< "$TEST_FILES"

# If pytest is available and there are Python tests, run twice with different seeds
PY_TEST_FILES=$(echo "$TEST_FILES" | grep -E 'test_.*\.py$|.*_test\.py$' || true)
if [ -n "$PY_TEST_FILES" ] && command -v pytest >/dev/null 2>&1; then
  if pytest --help 2>/dev/null | grep -q randomly; then
    echo "Running pytest twice with different seeds to detect flakiness..."
    run1=$(mktemp)
    run2=$(mktemp)
    pytest -q --randomly-seed=1234 >/dev/null 2>&1 && echo "PASS" > "$run1" || echo "FAIL" > "$run1"
    pytest -q --randomly-seed=5678 >/dev/null 2>&1 && echo "PASS" > "$run2" || echo "FAIL" > "$run2"
    if [ "$(cat "$run1")" != "$(cat "$run2")" ]; then
      echo "FAIL FM-10: test results differ across seeds (flaky suite)"
      fail=1
    else
      echo "OK FM-10: suite stable across seeds"
    fi
    rm -f "$run1" "$run2"
  else
    echo "INFO FM-10: pytest-randomly not installed; skipping seed-variation run"
  fi
fi

[ "$fail" -eq 0 ] && echo "OK FM-10: tests look deterministic"
exit $fail
