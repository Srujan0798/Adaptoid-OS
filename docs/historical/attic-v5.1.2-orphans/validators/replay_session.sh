#!/usr/bin/env bash
# replay_session.sh — Reconstruct context from events.jsonl for wake() resume.
# Usage: replay_session.sh <wave> <task> [N=10]
set -uo pipefail

WAVE="${1:?usage: replay_session.sh <wave> <task> [N]}"
TASK="${2:?}"
N="${3:-10}"

EVENT_FILE="orchestrator/memory/session/${WAVE}-${TASK}.events.jsonl"

if [ ! -f "$EVENT_FILE" ]; then
  echo "No session log found: $EVENT_FILE"
  echo "Start fresh or check wave/task name."
  exit 1
fi

TOTAL=$(wc -l < "$EVENT_FILE" | tr -d ' ')
echo "=== Session Replay: $WAVE / $TASK ==="
echo "Total events: $TOTAL  |  Showing last $N"
echo ""

# Last N events, pretty-printed
tail -n "$N" "$EVENT_FILE" | while IFS= read -r line; do
  TS=$(echo "$line" | grep -oE '"ts": "[^"]+"' | cut -d'"' -f4)
  ID=$(echo "$line" | grep -oE '"id": "[^"]+"' | cut -d'"' -f4)
  TYPE=$(echo "$line" | grep -oE '"type": "[^"]+"' | cut -d'"' -f4)
  printf "  %s  %-22s  %s\n" "$TS" "$ID" "$TYPE"
done

# Derive status
LAST_TYPE=$(tail -n 1 "$EVENT_FILE" | grep -oE '"type": "[^"]+"' | cut -d'"' -f4)
echo ""
echo "Current inferred state: $LAST_TYPE"

# Pending review?
PENDING=$(grep '"type": "report.received"' "$EVENT_FILE" | tail -n 1 | grep -oE '"task": "[^"]+"' | cut -d'"' -f4)
if [ -n "$PENDING" ]; then
  echo "Pending review: $PENDING"
fi

echo ""
echo "To resume: open Claude Code/Kimi in this dir, read HANDOFF.md + kernel, then proceed."
