#!/usr/bin/env bash
# Release gate for Adaptoid OS product kit.
# Usage: bash scripts/ship_check.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
rc=0

echo "========== ADAPTOID SHIP CHECK =========="

run() {
  local name="$1"; shift
  echo ""
  echo "── $name ──"
  if "$@"; then
    echo "OK $name"
  else
    echo "FAIL $name"
    rc=1
  fi
}

run "dogfood" bash validators/dogfood.sh
run "tests" bash tests/run_tests.sh
run "bench" bash benchmarks/run_bench.sh
run "calibration-smoke" bash calibration/run_calibration_smoke.sh
run "conductor-unit" python3 -c "
from pathlib import Path
import tempfile, subprocess, sys
root = Path('.').resolve()
# syntax / help
r = subprocess.run([sys.executable, 'conductor/conductor.py', '-h'], capture_output=True)
assert r.returncode == 0
"

echo ""
echo "========================================="
if [ "$rc" -eq 0 ]; then
  echo "SHIP CHECK: PASS ✅  Product kit is ready."
else
  echo "SHIP CHECK: FAIL ❌  Fix above before tagging release."
fi
exit "$rc"
