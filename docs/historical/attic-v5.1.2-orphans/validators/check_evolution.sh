#!/usr/bin/env bash
# check_evolution.sh — Validates the Evolution Engine protocol (GEPA + Hermes loops).
# Usage: check_evolution.sh [repo_root]
set -euo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/evolution-engine.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL evolution: $PROTO not found"; exit 1; }

grep -qi "GEPA" "$PROTO" || { echo "FAIL evolution: GEPA subsystem missing"; fail=1; }
grep -qi "Hermes" "$PROTO" || { echo "FAIL evolution: Hermes loop missing"; fail=1; }

for field in enabled max_variants eval_threshold canary_archetype max_cycles escalation_after_failures; do
  grep -q "$field" "$PROTO" || { echo "FAIL evolution: missing config field '$field'"; fail=1; }
done

for fm in FM-02 FM-05 FM-14 FM-16; do
  grep -q "$fm" "$PROTO" || { echo "FAIL evolution: missing failure mode '$fm'"; fail=1; }
done

grep -qi "rollback" "$PROTO" || { echo "FAIL evolution: no rollback rule (mutation safety)"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  evolution-engine protocol valid"
exit "$fail"
