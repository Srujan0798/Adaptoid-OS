#!/usr/bin/env bash
# FM-09 — False status / misframing.
# Flags claim words without an accompanying evidence block in worker reports.
# Usage: check_status_claims.sh [project_root] [--fix] [--dry-run]
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
REPORTS_DIR="$ROOT/work/reports"

if [ ! -d "$REPORTS_DIR" ]; then
  echo "OK FM-09: no worker reports to check"
  exit 0
fi

while IFS= read -r report; do
  # Find claim words not followed by a code block or evidence section
  if grep -iqE '\b(done|passed?|works?|complete|green|fixed)\b' "$report"; then
    has_evidence=0
    # Look for evidence markers: ``` output, Evidence:, Acceptance:, Ran:, Command:
    if grep -iqE '^```|^##+ (Evidence|Acceptance|Verification|Commands? Ran)|^[-*] (Evidence|Ran|Command):' "$report"; then
      has_evidence=1
    fi
    if [ "$has_evidence" -eq 0 ]; then
      echo "FAIL FM-09: $report makes status claims without an evidence block"
      fail=1
    fi
  fi

  # Result=DONE with unchecked acceptance boxes
  if grep -iqE '^[-*]*\s*Result\s*[:=]\s*DONE' "$report"; then
    unchecked=$(grep -cE '^\s*- \[ \]' "$report" 2>/dev/null || echo 0)
    if [ "$unchecked" -gt 0 ]; then
      echo "FAIL FM-09: $report claims DONE but has $unchecked unchecked acceptance items"
      fail=1
    fi
  fi
done < <(find "$REPORTS_DIR" -name '*.md' 2>/dev/null)

[ "$fail" -eq 0 ] && echo "OK FM-09: status claims backed by evidence"
exit $fail
