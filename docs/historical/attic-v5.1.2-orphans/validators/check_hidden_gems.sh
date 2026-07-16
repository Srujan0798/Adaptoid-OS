#!/usr/bin/env bash
# check_hidden_gems.sh — Validates the Hidden Gems protocol + catalog (≥30 scored entries).
# Usage: check_hidden_gems.sh [repo_root]
set -euo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/hidden-gems.md"
GEMS="$ROOT/reference/ecosystem/hidden-gems.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL hidden-gems: $PROTO not found"; exit 1; }
[ -f "$GEMS" ] || { echo "FAIL hidden-gems: catalog $GEMS not found"; exit 1; }

for criterion in "Harness fit" "Verifiability" "Documentation quality" "Active maintenance" "Differentiation"; do
  grep -qi "$criterion" "$PROTO" || { echo "FAIL hidden-gems: missing criterion '$criterion'"; fail=1; }
done

for field in enabled minimum_score stale_days; do
  grep -q "$field" "$PROTO" || { echo "FAIL hidden-gems: missing config field '$field'"; fail=1; }
done

for fm in FM-06 FM-12 FM-15; do
  grep -q "$fm" "$PROTO" || { echo "FAIL hidden-gems: missing failure mode '$fm'"; fail=1; }
done

ENTRIES=$(grep -cE '^\| [0-9]+ \|' "$GEMS" || true)
if [ "$ENTRIES" -lt 30 ]; then
  echo "FAIL hidden-gems: catalog has $ENTRIES entries (<30)"
  fail=1
fi

[ "$fail" -eq 0 ] && echo "OK  hidden-gems protocol valid ($ENTRIES catalog entries)"
exit "$fail"
