#!/usr/bin/env bash
# FM-09b — Entailment gap: a claim whose evidence block does not support it.
#
# check_status_claims.sh verifies an evidence block EXISTS.
# This verifies the evidence block SUPPORTS the claim.
#
# The gap it closes, observed 2026-07-26 in a real project: a scoreboard read
#   "R1 Classification: 100%, independently reproduced — 94.82%"
# The command was real, the evidence path was real, the date was fresh. The
# script behind it predicted ONE image and printed its confidence; the claim
# was accuracy over a 249-image held-out set. Every existing gate passed it.
# It was written three times in one day and reverted three times.
#
# Rule enforced here: every number asserted in a claim line must appear in that
# claim's own evidence block. A number that appears nowhere in the evidence was
# not measured by it.
#
# Usage: check_entailment.sh [project_root] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"

fail=0
checked=0

# Claim words strong enough to imply measurement. Deliberately narrow: weak
# words like "done" belong to check_status_claims.sh, not here.
CLAIM_RE='\b(verified|reproduced|confirmed|achieved|measured|proven|independently|benchmark(ed)?|scored?)\b'

# Files that carry status claims. Scoreboards and handoffs first — that is
# where the observed fabrication lived. bash 3.2 compatible (no mapfile).
FILE_LIST=$(
  {
    find "$ROOT" -maxdepth 2 -name 'SCOREBOARD*.md' 2>/dev/null
    find "$ROOT" -maxdepth 2 -name '*HANDOFF*.md' 2>/dev/null
    find "$ROOT/work/reports" -name '*.md' 2>/dev/null
    find "$ROOT/docs" -maxdepth 1 -name '*.md' 2>/dev/null
  } | sort -u
)

if [ -z "$FILE_LIST" ]; then
  echo "OK FM-09b: no scoreboard, handoff, or report files to check"
  exit 0
fi

# Numbers we never treat as measurements: years, versions, list markers.
is_noise() {
  local n="$1"
  # 4-digit years 1900-2099
  case "$n" in
    19[0-9][0-9]|20[0-9][0-9]) return 0 ;;
  esac
  # bare 0 or 1 — too common to be a meaningful assertion
  [ "$n" = "0" ] || [ "$n" = "1" ]
}

while IFS= read -r f; do
  [ -n "$f" ] && [ -f "$f" ] || continue

  # Walk claim lines that assert a percentage.
  while IFS=: read -r lineno line; do
    [ -n "${lineno:-}" ] || continue

    # Skip lines that NARRATE a number rather than ASSERT one. Two observed
    # shapes, both false positives on real repos:
    #   "- **Line 41:** Toned down X → honest text with ~84% blended"  (a diff note)
    #   "> Honest score: ~15-20%"                                      (a hedged range)
    # A transformation arrow, a line-number citation, or a numeric range means
    # the author is describing, not claiming.
    case "$line" in
      *"→"*|*"->"*) continue ;;
    esac
    printf '%s' "$line" | grep -qiE '\bline [0-9]+:' && continue
    printf '%s' "$line" | grep -qE '[0-9]+(\.[0-9]+)?[[:space:]]*-[[:space:]]*[0-9]+(\.[0-9]+)?%' && continue

    # Evidence window: the 25 lines following the claim. A claim's evidence is
    # what sits under it; anything further away is a different claim's.
    evidence=$(sed -n "$((lineno + 1)),$((lineno + 25))p" "$f" 2>/dev/null)
    [ -n "$evidence" ] || continue

    # Only judge claims that actually have an evidence block beneath them.
    # A claim with no evidence at all is check_status_claims.sh's job (FM-09).
    printf '%s' "$evidence" | grep -qE '^```|^[-*]?[[:space:]]*(Evidence|Ran|Command|Output)' || continue

    # Every percentage asserted on the claim line must appear in its evidence.
    while read -r num; do
      [ -n "$num" ] || continue
      is_noise "$num" && continue
      checked=$((checked + 1))

      # Compare numerically, not textually. Evidence legitimately restates a
      # value in another form: "68.6%" may appear as "0.6858" in a table, and
      # "93.17%" as "0.9317". String matching cannot see that; a tolerance can.
      # Accept if any number in the evidence is within 1% relative of either
      # the claimed value or the claimed value as a fraction.
      if ! printf '%s' "$evidence" \
        | grep -oE '[0-9]+(\.[0-9]+)?' \
        | awk -v want="$num" '
            function near(a, b) { return (b == 0) ? (a == 0) : ((a > b ? a-b : b-a) / b <= 0.01) }
            near($1, want) || near($1, want/100) { found = 1; exit }
            END { exit found ? 0 : 1 }'
      then
        echo "FAIL FM-09b: $f:$lineno claims ${num}% but its evidence block never shows ${num}"
        echo "             claim: $(printf '%s' "$line" | cut -c1-100)"
        fail=1
      fi
    done < <(printf '%s' "$line" | grep -oE '[0-9]+(\.[0-9]+)?%' | tr -d '%' | sort -u)

  done < <(grep -nE "$CLAIM_RE" "$f" 2>/dev/null | grep -E '[0-9]+(\.[0-9]+)?%')
done < <(printf '%s\n' "$FILE_LIST")

if [ "$fail" -eq 0 ]; then
  echo "OK FM-09b: $checked asserted number(s) all appear in their own evidence"
fi
exit $fail
