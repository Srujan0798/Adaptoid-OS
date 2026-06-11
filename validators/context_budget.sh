#!/usr/bin/env bash
# FM-04 — Context bloat. FM-15 — Context compaction prevention. Measures always-loaded kernel size.
# Usage: context_budget.sh [project_root] [--fix] [--dry-run]
# Note: --fix trims oversized files by moving sections to protocols/ (interactive, use --dry-run first).
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

total=0
for f in CLAUDE.md KIMI.md HANDOFF.md HIERARCHY.md; do
  if [ -f "$ROOT/$f" ]; then
    bytes=$(wc -c < "$ROOT/$f")
    toks=$((bytes / 4))
    total=$((total + toks))
    printf "  %-14s ~%5d tokens\n" "$f" "$toks"
  fi
done
echo "  TOTAL kernel ~$total tokens"

if   [ "$total" -gt 12000 ]; then
  echo "FAIL FM-04: kernel > 12K tokens — move detail to protocols/ or docs/"
  if [ "$FIX" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would suggest moving non-essential sections from largest file to protocols/"
    else
      largest=$(find "$ROOT" -maxdepth 1 \( -name 'CLAUDE.md' -o -name 'KIMI.md' -o -name 'HANDOFF.md' -o -name 'HIERARCHY.md' \) -exec wc -c {} + 2>/dev/null | sort -n | tail -1 | awk '{print $2}')
      echo "  SUGGEST: review $largest — move sections >500 tokens to protocols/ or docs/"
    fi
  fi
  exit 1
elif [ "$total" -gt 8000  ]; then
  echo "WARN FM-04: kernel > 8K tokens — trim toward 8K"; exit 0
else
  echo "OK FM-04: kernel within budget"; exit 0
fi
