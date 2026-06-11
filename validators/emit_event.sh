#!/usr/bin/env bash
# emit_event.sh — Append-only event log for Brain/Hands/Session triad.
# Usage: emit_event.sh <wave> <task> <type> [key=value ...]
# Example: emit_event.sh wave-1 01-backend-skeleton task.dispatched file=work/wave-1/01-backend-skeleton.md
set -uo pipefail

WAVE="${1:?usage: emit_event.sh <wave> <task> <type> [k=v ...]}"
TASK="${2:?}"
ETYPE="${3:?}"
shift 3

SESSION_DIR="orchestrator/memory/session"
mkdir -p "$SESSION_DIR"

EVENT_FILE="$SESSION_DIR/${WAVE}-${TASK}.events.jsonl"

# Build JSON payload from k=v pairs
PAYLOAD=""
for kv in "$@"; do
  k="${kv%%=*}"
  v="${kv#*=}"
  [ -n "$PAYLOAD" ] && PAYLOAD="$PAYLOAD, "
  PAYLOAD="$PAYLOAD\"$k\": \"$v\""
done

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
ID="evt-$(date +%s%N | cut -c1-12)"

# Hash chain: each event includes the previous event's hash (tamper evidence).
# Genesis (first event in file) chains from 64 zeros.
PREV_HASH="sha256:0000000000000000000000000000000000000000000000000000000000000000"
if [ -s "$EVENT_FILE" ]; then
  LAST_HASH=$(tail -n 1 "$EVENT_FILE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('hash',''))" 2>/dev/null || echo "")
  [ -n "$LAST_HASH" ] && PREV_HASH="$LAST_HASH"
fi

# Compute hash of the event (including prev_hash) for the audit chain
EVENT_LINE=$(printf '{"ts": "%s", "id": "%s", "type": "%s", "wave": "%s", "task": "%s", "prev_hash": "%s"%s}' \
  "$TS" "$ID" "$ETYPE" "$WAVE" "$TASK" "$PREV_HASH" "${PAYLOAD:+, $PAYLOAD}")
HASH="sha256:$(echo "$EVENT_LINE" | sha256sum | awk '{print $1}')"

# Append hash to the line
printf '%s\n' "$EVENT_LINE" | sed "s|}$|, \"hash\": \"$HASH\"}|" >> "$EVENT_FILE"

echo "Emitted $ID → $EVENT_FILE"
