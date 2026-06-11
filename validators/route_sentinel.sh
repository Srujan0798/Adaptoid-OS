#!/usr/bin/env bash
# FM-16 — Route Sentinel. Validates DAG_TRANSITIONS map in adaptoid.config.yaml.
# Usage: route_sentinel.sh [project_root] [--fix] [--dry-run]
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

CONFIG="$ROOT/adaptoid.config.yaml"
fail=0

if [ ! -f "$CONFIG" ]; then
  echo "OK route-sentinel: no adaptoid.config.yaml found (optional)"
  exit 0
fi

# Check dag_transitions block exists
if ! grep -qE '^dag_transitions:' "$CONFIG"; then
  echo "WARN route-sentinel: adaptoid.config.yaml missing dag_transitions block"
  exit 0
fi

# Extract nodes from dag_transitions (simple YAML heuristic)
nodes=$(awk '/^dag_transitions:/{flag=1;next} /^[a-z]/{flag=0} flag{print}' "$CONFIG" | grep -oE '^\s+\w+:' | tr -d ' :' | sort -u)

if [ -z "$nodes" ]; then
  echo "FAIL route-sentinel: dag_transitions block present but empty"
  exit 1
fi

# Check for self-loops
while IFS= read -r node; do
  [ -z "$node" ] && continue
  self_loop=$(awk "/^  $node:/{flag=1;next} /^  [a-z]/{flag=0} flag" "$CONFIG" | grep -cE "allowed_next:.*\\b$node\\b" || echo 0)
  if [ "$self_loop" -gt 0 ]; then
    echo "FAIL route-sentinel: self-loop detected on node '$node'"
    fail=1
  fi
done <<< "$nodes"

# Check retry limits are present
missing_retry=$(awk '/^dag_transitions:/{flag=1;next} /^[a-z]/{flag=0} flag' "$CONFIG" | grep -cE 'max_retries:' || echo 0)
total_nodes=$(echo "$nodes" | wc -l | tr -d ' ')
if [ "$missing_retry" -lt "$total_nodes" ]; then
  echo "WARN route-sentinel: some dag_transitions nodes missing max_retries"
fi

[ "$fail" -eq 0 ] && echo "OK route-sentinel: DAG transitions valid"
exit $fail
