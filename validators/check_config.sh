#!/usr/bin/env bash
# FM-06 — Config revert. Diffs critical config against a committed lock; flags hardcoded params.
# Usage: check_config.sh [project_root] [--fix] [--dry-run]
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

CFG=$(ls "$ROOT"/configs/default.* 2>/dev/null | head -1)
LOCK="$ROOT/configs/default.lock"

if [ -n "${CFG:-}" ] && [ -f "$LOCK" ]; then
  while IFS='=' read -r key expected; do
    [ -z "$key" ] && continue
    actual=$(grep -E "^[[:space:]]*$key[:=]" "$CFG" | head -1 | sed -E "s/.*[:=][[:space:]]*//; s/[[:space:]]*#.*//")
    if [ -n "$actual" ] && [ "$actual" != "$expected" ]; then
      echo "FAIL FM-06: config drift — $key=$actual but lock expects $expected"
      if [ "$FIX" -eq 1 ]; then
        if [ "$DRY" -eq 1 ]; then
          echo "  [DRY-RUN] would update $key to $expected in $CFG"
        else
          # Update the value in config
          sed -i.bak -E "s/^([[:space:]]*$key[:=][[:space:]]*).*/\1$expected/" "$CFG"
          rm -f "$CFG.bak"
          echo "  FIXED: updated $key → $expected in $CFG"
        fi
      fi
      fail=1
    fi
  done < "$LOCK"
fi

# Flag hardcoded critical params
hard=$(grep -rInE '(epochs|k_inner|batch_size|lr|alpha)\s*=\s*[0-9.]+' "$ROOT/src" "$ROOT/experiments" 2>/dev/null \
       | grep -viE 'cfg\.|config\.|settings\.|self\.' || true)
if [ -n "$hard" ]; then
  echo "WARN FM-06: possible hardcoded params (should read from config):"
  echo "$hard" | head -10 | sed 's/^/  /'
fi

[ "$fail" -eq 0 ] && echo "OK FM-06: config matches lock"
exit $fail
