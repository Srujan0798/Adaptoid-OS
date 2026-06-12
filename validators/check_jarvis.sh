#!/usr/bin/env bash
# check_jarvis.sh — Validates the Jarvis Mode protocol (proactive but never unilateral).
# Usage: check_jarvis.sh [repo_root]
set -uo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/jarvis-mode.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL jarvis: $PROTO not found"; exit 1; }

for behavior in "Intention prediction" "Pre-fetch" "Background sentry" "Polite interruption"; do
  grep -qi "$behavior" "$PROTO" || { echo "FAIL jarvis: missing behavior '$behavior'"; fail=1; }
done

for field in enabled sentry_interval_s prefetch_protocols approval_required_for; do
  grep -q "$field" "$PROTO" || { echo "FAIL jarvis: missing config field '$field'"; fail=1; }
done

for fm in FM-02 FM-08 FM-09 FM-13; do
  grep -q "$fm" "$PROTO" || { echo "FAIL jarvis: missing failure mode '$fm'"; fail=1; }
done

grep -qi "ask, don't act" "$PROTO" || { echo "FAIL jarvis: missing 'Ask, don't act' safety rule"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  jarvis-mode protocol valid"
exit "$fail"
