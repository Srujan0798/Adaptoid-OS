#!/usr/bin/env bash
# FM-18 / FM-20 — OAP Security. Policy packs cover active tools;
# MCP servers must be allowlisted (deny-by-default, FM-20-mcp-tool-trust.md).
# Usage: oap_security.sh [project_root] [--fix] [--dry-run]
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

POLICIES="$ROOT/policies"
CONFIG="$ROOT/adaptoid.config.yaml"
fail=0

if [ ! -d "$POLICIES" ]; then
  echo "WARN oap-security: no policies/ directory found (optional)"
  exit 0
fi

# Validate YAML syntax of all policy packs
while IFS= read -r f; do
  if ! python3 -c "import yaml; yaml.safe_load(open('$f'))" 2>/dev/null; then
    echo "FAIL oap-security: invalid YAML in $f"
    fail=1
  fi
done < <(find "$POLICIES" -name '*.yaml' 2>/dev/null)

# Check that default pack exists
if [ ! -f "$POLICIES/default.yaml" ]; then
  echo "WARN oap-security: no default.yaml policy pack"
fi

# Check that active tools from config are covered (heuristic)
if [ -f "$CONFIG" ]; then
  tools=$(grep -oE '\b(Read|Write|Edit|Bash|Grep|Glob|Agent|AgentSwarm)\b' "$CONFIG" | sort -u)
  if [ -n "$tools" ]; then
    while IFS= read -r tool; do
      covered=$(grep -rl "$tool" "$POLICIES" 2>/dev/null | head -1)
      if [ -z "$covered" ]; then
        echo "WARN oap-security: tool '$tool' in config has no matching policy"
      fi
    done <<< "$tools"
  fi
fi

# FM-20 — every configured MCP server needs policy coverage (deny-by-default)
if [ -f "$CONFIG" ]; then
  servers=$(sed -n 's/^mcp_servers:[[:space:]]*\[\(.*\)\]/\1/p' "$CONFIG" | tr ',' '\n' | tr -d ' "')
  for s in $servers; do
    [ -z "$s" ] && continue
    if ! grep -rqi "$s" "$POLICIES" 2>/dev/null; then
      echo "FAIL oap-security FM-20: MCP server '$s' has no policy coverage (deny-by-default)"
      fail=1
    fi
  done
fi

[ "$fail" -eq 0 ] && echo "OK oap-security: policy packs valid"
exit $fail
