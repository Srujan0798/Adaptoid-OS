#!/usr/bin/env bash
# FM-13 — Parallel collisions. Fails if two task briefs in a wave share a write target.
# Usage: check_dispatch_disjoint.sh <wave_dir> [--fix] [--dry-run]
# Note: --fix cannot auto-resolve collisions; it reports which tasks need re-planning.
set -uo pipefail
WAVE_DIR="${1:?usage: check_dispatch_disjoint.sh work/wave-N}"
shift || true

FIX=0
DRY=0
for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    --dry-run) DRY=1 ;;
  esac
done

tmp=$(mktemp)

for f in "$WAVE_DIR"/*.md; do
  [ -e "$f" ] || continue
  grep -iE 'CREATE:|MODIFY:' "$f" 2>/dev/null \
    | sed -E 's/.*(CREATE|MODIFY):\s*//I' | awk '{print $1}' \
    | while IFS= read -r p; do
        [ -n "$p" ] && echo "$p|$(basename "$f")" >> "$tmp"
      done
done

dups=$(cut -d'|' -f1 "$tmp" 2>/dev/null | sort | uniq -d)
rc=0
if [ -n "$dups" ]; then
  echo "FAIL FM-13: files claimed by multiple parallel briefs:"
  for d in $dups; do
    owners=$(grep "^$d|" "$tmp" | cut -d'|' -f2 | tr '\n' ' ')
    echo "  $d  ← $owners"
  done
  if [ "$FIX" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would require re-planning: make write sets disjoint or add dependencies"
    else
      echo "  ACTION REQUIRED: Re-plan these tasks so each file is touched by only one brief."
      echo "  Add dependency lines (e.g. 'Depends on: 01-*.md') to sequence colliding tasks."
    fi
  fi
  echo "  → make write sets disjoint, or sequence these tasks with a dependency."
  rc=1
else
  echo "OK FM-13: wave briefs have disjoint write sets"
fi
rm -f "$tmp"
exit $rc
