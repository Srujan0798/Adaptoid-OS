#!/usr/bin/env bash
# check_consciousness.sh — Validates the Consciousness Core protocol (functional self-monitoring).
# Usage: check_consciousness.sh [repo_root]
set -uo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/consciousness-core.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL consciousness: $PROTO not found"; exit 1; }

for field in enabled confidence_threshold irreversible_threshold cost_usd_limit latency_ms_limit; do
  grep -q "$field" "$PROTO" || { echo "FAIL consciousness: missing config field '$field'"; fail=1; }
done

for fm in FM-01 FM-09 FM-10 FM-17; do
  grep -q "$fm" "$PROTO" || { echo "FAIL consciousness: missing failure mode '$fm'"; fail=1; }
done

grep -qi "checkpoint" "$PROTO" || { echo "FAIL consciousness: no checkpoint table"; fail=1; }
grep -qi "evidence" "$PROTO" || { echo "FAIL consciousness: no evidence requirement"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  consciousness-core protocol valid"
exit "$fail"
