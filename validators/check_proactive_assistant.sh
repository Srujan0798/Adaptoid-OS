#!/usr/bin/env bash
# check_proactive_assistant.sh — Validates the Proactive Assistant protocol (proactive but never unilateral).
# Usage: check_proactive_assistant.sh [repo_root]
set -euo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/proactive-assistant.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL proactive_assistant: $PROTO not found"; exit 1; }

for behavior in "Intention prediction" "Pre-fetch" "Background sentry" "Polite interruption"; do
  grep -qi "$behavior" "$PROTO" || { echo "FAIL proactive_assistant: missing behavior '$behavior'"; fail=1; }
done

for field in enabled sentry_interval_s prefetch_protocols approval_required_for; do
  grep -q "$field" "$PROTO" || { echo "FAIL proactive_assistant: missing config field '$field'"; fail=1; }
done

for fm in FM-02 FM-08 FM-09 FM-13; do
  grep -q "$fm" "$PROTO" || { echo "FAIL proactive_assistant: missing failure mode '$fm'"; fail=1; }
done

grep -qi "ask, don't act" "$PROTO" || { echo "FAIL proactive_assistant: missing 'Ask, don't act' safety rule"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  proactive-assistant protocol valid"
exit "$fail"
