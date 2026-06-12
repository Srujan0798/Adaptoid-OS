#!/usr/bin/env bash
# check_fable5.sh — Validates the Fable 5 Workflows protocol (10 workflow patterns).
# Usage: check_fable5.sh [repo_root]
set -uo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/fable-5-workflows.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL fable5: $PROTO not found"; exit 1; }

COUNT=$(grep -cE '^\| [0-9]+ \| \*\*' "$PROTO" || true)
if [ "$COUNT" -lt 10 ]; then
  echo "FAIL fable5: expected ≥10 workflows, found $COUNT"
  fail=1
fi

for field in enabled default_workflow; do
  grep -q "$field" "$PROTO" || { echo "FAIL fable5: missing config field '$field'"; fail=1; }
done

for fm in FM-02 FM-09 FM-10 FM-11; do
  grep -q "$fm" "$PROTO" || { echo "FAIL fable5: missing failure mode '$fm'"; fail=1; }
done

grep -q "PROJECT-INTENT" "$PROTO" || { echo "FAIL fable5: workflows must start from typed intent"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  fable-5-workflows protocol valid ($COUNT workflows)"
exit "$fail"
