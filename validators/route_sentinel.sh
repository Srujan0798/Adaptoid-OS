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

# Extract transition *nodes* only (two-space indent keys under dag_transitions).
# Ignore nested keys like allowed_next / max_retries (four-space indent).
nodes=$(awk '
  /^dag_transitions:/ { flag=1; next }
  flag && /^[a-zA-Z]/ { flag=0 }
  flag && /^  [a-zA-Z0-9_-]+:/ {
    key=$1; sub(/:/,"",key); print key
  }
' "$CONFIG" | sort -u)

if [ -z "$nodes" ]; then
  echo "FAIL route-sentinel: dag_transitions block present but empty"
  exit 1
fi

# Check for self-loops
# Note: grep -c prints 0 and exits 1 on no match — never pair with `|| echo 0`
# (that yields "0\n0" and breaks integer comparison).
while IFS= read -r node; do
  [ -z "$node" ] && continue
  self_loop=$(awk "/^  ${node}:/{flag=1;next} /^  [a-zA-Z]/{flag=0} flag" "$CONFIG" | grep -cE "allowed_next:.*\\b${node}\\b" || true)
  self_loop=${self_loop//$'\n'/}
  self_loop=${self_loop:-0}
  if [ "$self_loop" -gt 0 ] 2>/dev/null; then
    echo "FAIL route-sentinel: self-loop detected on node '$node'"
    fail=1
  fi
done <<< "$nodes"

# Check retry limits are present (one max_retries per node)
retry_count=$(awk '
  /^dag_transitions:/ { flag=1; next }
  flag && /^[a-zA-Z]/ { flag=0 }
  flag && /max_retries:/ { c++ }
  END { print c+0 }
' "$CONFIG")
total_nodes=$(echo "$nodes" | grep -c . || true)
total_nodes=${total_nodes//$'\n'/}
total_nodes=${total_nodes:-0}
if [ "$retry_count" -lt "$total_nodes" ] 2>/dev/null; then
  echo "WARN route-sentinel: some dag_transitions nodes missing max_retries"
fi

[ "$fail" -eq 0 ] && echo "OK route-sentinel: DAG transitions valid"
exit $fail
