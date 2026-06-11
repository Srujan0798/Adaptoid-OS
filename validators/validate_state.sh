#!/usr/bin/env bash
# FM-01 — State drift. Fails on duplicate rows / headers / active-wave mismatch.
# Usage: validate_state.sh [project_root] [--fix] [--dry-run]
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

EXEC="$ROOT/plan/EXECUTION.md"
HAND="$ROOT/HANDOFF.md"
fail=0
fixes=()

if [ -f "$EXEC" ]; then
  # Duplicate status-table rows by wave id
  dups=$(grep -oE '^\| *[0-9]+ *\|' "$EXEC" | tr -d ' |' | sort | uniq -d)
  if [ -n "$dups" ]; then
    echo "FAIL FM-01: duplicate wave rows in EXECUTION.md: $(echo "$dups" | tr '\n' ' ')"
    if [ "$FIX" -eq 1 ]; then
      if [ "$DRY" -eq 1 ]; then
        echo "  [DRY-RUN] would remove duplicate rows keeping first occurrence"
      else
        tmp=$(mktemp)
        awk '!seen[$0]++' "$EXEC" > "$tmp" && mv "$tmp" "$EXEC"
        echo "  FIXED: removed duplicate rows"
      fi
    fi
    fail=1
  fi

  # Duplicate section headers
  hdrs=$(grep -E '^##+ ' "$EXEC" | sed 's/ *$//' | sort | uniq -d)
  if [ -n "$hdrs" ]; then
    echo "FAIL FM-01: duplicate headers in EXECUTION.md:"; echo "$hdrs"
    if [ "$FIX" -eq 1 ] && [ "$DRY" -eq 0 ]; then
      # Merge duplicate headers by keeping first, removing subsequent
      tmp=$(mktemp)
      awk '!seen[$0]++ || $0 !~ /^##+ /' "$EXEC" > "$tmp" && mv "$tmp" "$EXEC"
      echo "  FIXED: merged duplicate headers"
    elif [ "$FIX" -eq 1 ]; then
      echo "  [DRY-RUN] would merge duplicate headers"
    fi
    fail=1
  fi
fi

# Active wave consistency
if [ -f "$EXEC" ] && [ -f "$HAND" ]; then
  we=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$EXEC" | grep -oE '[0-9]+' | head -1)
  wh=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$HAND" | grep -oE '[0-9]+' | head -1)
  if [ -n "$we" ] && [ -n "$wh" ] && [ "$we" != "$wh" ]; then
    echo "FAIL FM-01: active wave mismatch — EXECUTION=$we HANDOFF=$wh"
    if [ "$FIX" -eq 1 ]; then
      if [ "$DRY" -eq 1 ]; then
        echo "  [DRY-RUN] would update HANDOFF.md active wave to $we (from EXECUTION.md)"
      else
        sed -i.bak -E "s/(active wave[^0-9]*)[0-9]+/\1$we/i" "$HAND"
        rm -f "$HAND.bak"
        echo "  FIXED: updated HANDOFF.md active wave → $we (from EXECUTION.md)"
      fi
    fi
    fail=1
  fi
fi

[ "$fail" -eq 0 ] && echo "OK FM-01: state files consistent"
exit $fail
