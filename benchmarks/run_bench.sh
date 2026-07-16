#!/usr/bin/env bash
# Adaptoid Core benchmarks — speed + correctness smoke suite.
# Usage: bash benchmarks/run_bench.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${TMPDIR:-/tmp}/adaptoid-bench-$$"
mkdir -p "$OUT_DIR"
RESULTS="$OUT_DIR/results.json"
rc=0

ts() { python3 -c 'import time; print(time.time())'; }

echo "=== Adaptoid benchmarks ==="
echo "workspace: $OUT_DIR"

# 1) Engine core-only latency
t0=$(ts)
python3 "$ROOT/adaptor/engine.py" \
  --brief "bench cli tool for log parsing" \
  --output "$OUT_DIR/core-proj" \
  --core-only \
  --host all \
  --skip-verify >/dev/null 2>"$OUT_DIR/engine.err"
t1=$(ts)
ENGINE_S=$(python3 -c "print(round($t1 - $t0, 3))")
echo "engine_core_all_hosts_s=$ENGINE_S"

# 2) Host surfaces present
HOST_OK=1
for f in AGENTS.md CLAUDE.md HANDOFF.md kernel/PRINCIPLES.md \
         .cursor/rules/adaptoid.mdc orchestrator/scripts/preflight.sh; do
  if [ ! -e "$OUT_DIR/core-proj/$f" ]; then
    echo "FAIL missing $f"
    HOST_OK=0
    rc=1
  fi
done
echo "host_surfaces_ok=$HOST_OK"

# 3) Preflight on generated project
t0=$(ts)
if bash "$OUT_DIR/core-proj/orchestrator/scripts/preflight.sh" "$OUT_DIR/core-proj" \
    >"$OUT_DIR/preflight.out" 2>&1; then
  PRE_OK=1
else
  PRE_OK=0
  rc=1
fi
t1=$(ts)
PRE_S=$(python3 -c "print(round($t1 - $t0, 3))")
echo "preflight_ok=$PRE_OK preflight_s=$PRE_S"

# 4) Conductor init + dispatch stub
t0=$(ts)
python3 "$ROOT/conductor/conductor.py" init-wave --project "$OUT_DIR/core-proj" --wave wave-1 -n 3 \
  >"$OUT_DIR/init.out" 2>&1
python3 "$ROOT/conductor/conductor.py" check-disjoint --project "$OUT_DIR/core-proj" --wave wave-1 \
  >"$OUT_DIR/disjoint.out" 2>&1
python3 "$ROOT/conductor/conductor.py" dispatch --project "$OUT_DIR/core-proj" --wave wave-1 --mode stub \
  >"$OUT_DIR/dispatch.out" 2>&1
t1=$(ts)
COND_S=$(python3 -c "print(round($t1 - $t0, 3))")
REPORTS=$(find "$OUT_DIR/core-proj/work/reports" -name '*.report.md' 2>/dev/null | wc -l | tr -d ' ')
echo "conductor_s=$COND_S reports=$REPORTS"
[ "$REPORTS" -ge 3 ] || { echo "FAIL expected >=3 reports"; rc=1; }

# 5) Dogfood (kit integrity)
t0=$(ts)
if bash "$ROOT/validators/dogfood.sh" >"$OUT_DIR/dogfood.out" 2>&1; then
  DOG_OK=1
else
  DOG_OK=0
  rc=1
fi
t1=$(ts)
DOG_S=$(python3 -c "print(round($t1 - $t0, 3))")
echo "dogfood_ok=$DOG_OK dogfood_s=$DOG_S"

# 6) Write results JSON
python3 - <<PY
import json
from pathlib import Path
data = {
  "engine_core_all_hosts_s": float("$ENGINE_S"),
  "host_surfaces_ok": bool($HOST_OK),
  "preflight_ok": bool($PRE_OK),
  "preflight_s": float("$PRE_S"),
  "conductor_s": float("$COND_S"),
  "reports": int("$REPORTS"),
  "dogfood_ok": bool($DOG_OK),
  "dogfood_s": float("$DOG_S"),
  "pass": $rc == 0,
}
Path("$RESULTS").write_text(json.dumps(data, indent=2))
print(json.dumps(data, indent=2))
PY

# Copy last results into benchmarks/ for humans
cp "$RESULTS" "$ROOT/benchmarks/last_results.json" 2>/dev/null || true

echo ""
if [ "$rc" -eq 0 ]; then
  echo "BENCH: PASS ✅"
else
  echo "BENCH: FAIL ❌  see $OUT_DIR"
fi
# keep OUT_DIR for debugging on fail
[ "$rc" -eq 0 ] && rm -rf "$OUT_DIR"
exit "$rc"
