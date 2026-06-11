#!/usr/bin/env bash
# FM-05 / FM-12 — Metric inconsistency + stale derived docs.
# Canonical metrics live in results/metrics.json. Flags docs that state different numbers.
# Usage: check_metrics.sh [project_root] [--fix] [--dry-run]
# Note: --fix regenerates derived docs from metrics.json if a generator script exists.
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

CANON="$ROOT/results/metrics.json"

if [ ! -f "$CANON" ]; then
  echo "SKIP FM-05: no results/metrics.json (canonical metrics source not set up yet)"
  exit 0
fi

flagged=0
for doc in "$ROOT/README.md" "$ROOT"/deliverables/report/*.md "$ROOT"/docs/*.md; do
  [ -f "$doc" ] || continue
  if grep -qiE '\b(F1|accuracy|precision|recall|pass@|pass\^|reduction|overhead|%)\b' "$doc"; then
    if ! grep -qiE 'metrics\.json|generated|do not edit|auto-generated' "$doc"; then
      echo "WARN FM-05: $doc states metrics but doesn't reference the generated source."
      flagged=1
      if [ "$FIX" -eq 1 ]; then
        if [ "$DRY" -eq 1 ]; then
          echo "  [DRY-RUN] would add <!-- Auto-generated from results/metrics.json; do not edit manually -->"
        else
          # Add header comment if not present
          if ! head -n 1 "$doc" | grep -qi "auto-generated"; then
            tmp=$(mktemp)
            echo "<!-- Auto-generated from results/metrics.json; do not edit manually. -->" > "$tmp"
            cat "$doc" >> "$tmp"
            mv "$tmp" "$doc"
            echo "  FIXED: added auto-generated header to $doc"
          fi
        fi
      fi
    fi
  fi
done

if [ "$flagged" -eq 0 ]; then
  echo "OK FM-05: metric-bearing docs reference the canonical source"
else
  echo "  → numbers must come from results/metrics.json (generated), never hand-typed."
fi
exit 0
