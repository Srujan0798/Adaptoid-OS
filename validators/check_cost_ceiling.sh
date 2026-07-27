#!/usr/bin/env bash
# FM-19 — Cost / token runaway. Every generated project must declare a cost ceiling.
# Hosts enforce their own budget flags; this gate forces the ceiling to be stated
# so "how much may this wave spend?" always has one answer (FM-05: one fact, one home).
# Usage: check_cost_ceiling.sh [project_root]
set -uo pipefail
ROOT="${1:-.}"
CONFIG="$ROOT/adaptoid.config.yaml"

if [ ! -f "$CONFIG" ]; then
  echo "OK FM-19: no adaptoid.config.yaml (kit repo / Lite) — skipped"
  exit 0
fi

max=$(grep -E '^[[:space:]]*max_usd_per_wave:' "$CONFIG" | head -1 | sed 's/.*:[[:space:]]*//' | tr -d '"')
if [ -z "$max" ]; then
  echo "FAIL FM-19: no cost ceiling in adaptoid.config.yaml — add cost.max_usd_per_wave"
  exit 1
fi
case "$max" in
  ''|*[!0-9.]*)
    echo "FAIL FM-19: cost.max_usd_per_wave is not a number: '$max'"
    exit 1
    ;;
esac
echo "OK FM-19: cost ceiling declared (max_usd_per_wave=$max)"
exit 0
