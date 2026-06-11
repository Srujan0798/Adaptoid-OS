#!/usr/bin/env bash
# STALE_CHECK.sh — Flags ecosystem catalog files older than N days.
# Usage: STALE_CHECK.sh [max_days] [ecosystem_dir]
set -uo pipefail

MAX_DAYS="${1:-90}"
ECO_DIR="${2:-$(cd "$(dirname "$0")" && pwd)}"

stale=0
total=0

for f in "$ECO_DIR"/*.md; do
  [ -e "$f" ] || continue
  total=$((total + 1))

  # Extract last-verified from YAML frontmatter
  verified=$(head -n 10 "$f" | grep -oE 'last-verified:[[:space:]]*[0-9]{4}-[0-9]{2}-[0-9]{2}' | sed 's/.*:[[:space:]]*//' || true)

  if [ -z "$verified" ]; then
    echo "WARN: $(basename "$f") — no last-verified date in frontmatter"
    stale=$((stale + 1))
    continue
  fi

  # Calculate days since verified (macOS / Linux compatible)
  verified_epoch=$(date -j -f "%Y-%m-%d" "$verified" "+%s" 2>/dev/null || date -d "$verified" "+%s" 2>/dev/null || echo 0)
  now_epoch=$(date +%s)
  days_old=$(((now_epoch - verified_epoch) / 86400))

  if [ "$days_old" -gt "$MAX_DAYS" ]; then
    echo "STALE: $(basename "$f") — last verified $verified ($days_old days ago)"
    stale=$((stale + 1))
  fi
done

echo ""
echo "Checked: $total files  |  Stale: $stale  |  Threshold: ${MAX_DAYS} days"

if [ "$stale" -gt 0 ]; then
  echo ""
  echo "Action: Re-verify stale entries before relying on them (FM-12 applied to the library itself)."
  exit 1
fi

echo "OK: all ecosystem files fresh"
exit 0
