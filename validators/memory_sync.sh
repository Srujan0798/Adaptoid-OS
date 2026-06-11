#!/usr/bin/env bash
# Memory-bank index + rotation.
# Usage: memory_sync.sh [project_root] [--index|--rotate|--search <query>]
set -uo pipefail
ROOT="${1:-.}"
shift || true

ACTION="index"
QUERY=""

for arg in "$@"; do
  case "$arg" in
    --index) ACTION="index" ;;
    --rotate) ACTION="rotate" ;;
    --search) ACTION="search" ;;
    *) [ "$ACTION" = "search" ] && QUERY="$arg" ;;
  esac
done

BANK="$ROOT/memory-bank"
if [ ! -d "$BANK" ]; then
  echo "OK memory-sync: no memory-bank found (optional)"
  exit 0
fi

if [ "$ACTION" = "index" ]; then
  echo "=== Memory Bank Index ==="
  for dir in facts decisions lessons sessions evidence snapshots; do
    count=$(find "$BANK/$dir" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
    echo "  $dir: $count entries"
  done
  exit 0
fi

if [ "$ACTION" = "rotate" ]; then
  now=$(date +%s)
  found=0
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    ttl=$(grep -m1 '^ttl_days:' "$f" 2>/dev/null | awk '{print $2}' || echo 90)
    verified=$(grep -m1 '^verified:' "$f" 2>/dev/null | awk '{print $2}' || echo "")
    if [ -n "$verified" ]; then
      vsec=$(date -j -f "%Y-%m-%d" "$verified" +%s 2>/dev/null || date -d "$verified" +%s 2>/dev/null || echo 0)
      age=$(( (now - vsec) / 86400 ))
      if [ "$age" -gt "$ttl" ]; then
        echo "STALE: $f (age=${age}d > ttl=${ttl}d)"
        found=1
      fi
    fi
  done < <(find "$BANK" -name '*.md' 2>/dev/null)
  if [ "$found" -eq 0 ]; then
    echo "OK memory-sync: no stale entries"
  fi
  exit 0
fi

if [ "$ACTION" = "search" ]; then
  if [ -z "$QUERY" ]; then
    echo "WARN memory-sync: search requires a query"
    exit 1
  fi
  echo "=== Search: $QUERY ==="
  grep -ril "$QUERY" "$BANK" 2>/dev/null | head -20
  exit 0
fi
