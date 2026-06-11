#!/usr/bin/env bash
# FM-14 — Lost handoff (cold new session).
# Ensures HANDOFF.md exists, is fresh, and matches EXECUTION.md.
# Usage: check_handoff.sh [project_root] [--fix] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"
FIX=0
DRY=0
shift || true

for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    --dry-run) DRY=1 ;;
  esac
done

fail=0
HAND="$ROOT/HANDOFF.md"
EXEC="$ROOT/plan/EXECUTION.md"

if [ ! -f "$HAND" ]; then
  echo "FAIL FM-14: HANDOFF.md missing — new sessions will start cold"
  fail=1
fi

# Active wave consistency with EXECUTION.md
if [ -f "$HAND" ] && [ -f "$EXEC" ]; then
  wh=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$HAND" | grep -oE '[0-9]+' | head -1)
  we=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$EXEC" | grep -oE '[0-9]+' | head -1)
  if [ -n "$wh" ] && [ -n "$we" ] && [ "$wh" != "$we" ]; then
    echo "FAIL FM-14: HANDOFF active wave ($wh) != EXECUTION.md active wave ($we)"
    if [ "$FIX" -eq 1 ]; then
      if [ "$DRY" -eq 1 ]; then
        echo "  [DRY-RUN] would update HANDOFF.md active wave to $we"
      else
        sed -i.bak -E "s/(active wave[^0-9]*)[0-9]+/\1$we/i" "$HAND"
        rm -f "$HAND.bak"
        echo "  FIXED: updated HANDOFF.md active wave → $we"
      fi
    fi
    fail=1
  fi
fi

# Events.jsonl exists for active wave
if [ -f "$HAND" ]; then
  wave=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$HAND" | grep -oE '[0-9]+' | head -1)
  if [ -n "$wave" ]; then
    events=$(find "$ROOT/orchestrator/memory/session" -name "wave-${wave}-*.events.jsonl" 2>/dev/null | head -1)
    if [ -z "$events" ]; then
      echo "WARN FM-14: no events.jsonl found for active wave $wave"
    fi
  fi
fi

# Stale handoff check: HANDOFF.md should be newer than the last merge commit if in git
if [ -f "$HAND" ] && [ -d "$ROOT/.git" ]; then
  last_commit=$(cd "$ROOT" && git log -1 --format=%ct 2>/dev/null || echo 0)
  hand_mtime=$(stat -f %m "$HAND" 2>/dev/null || stat -c %Y "$HAND" 2>/dev/null || echo 0)
  if [ "$last_commit" -gt "$hand_mtime" ]; then
    echo "WARN FM-14: HANDOFF.md older than last merge commit — may be stale"
  fi
fi

[ "$fail" -eq 0 ] && echo "OK FM-14: handoff file present and consistent"
exit $fail
