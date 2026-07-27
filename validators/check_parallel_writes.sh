#!/usr/bin/env bash
# FM-13 — Parallel collisions. Static disjoint-writes check across a wave's task briefs.
# Mirrors conductor.py check_disjoint so preflight can gate without dispatching.
# Usage: check_parallel_writes.sh [project_root]
set -uo pipefail
ROOT="${1:-.}"
fail=0

for wave_dir in "$ROOT"/work/*/; do
  [ -d "$wave_dir" ] || continue
  [ "$(basename "$wave_dir")" = "reports" ] && continue
  tasks_dir="$wave_dir"
  [ -d "${wave_dir}tasks" ] && tasks_dir="${wave_dir}tasks"

  tmp=$(mktemp)
  for f in "$tasks_dir"/*.md; do
    [ -f "$f" ] || continue
    w=$(grep -iE '^writes[[:space:]]*:' "$f" | head -1 | sed 's/^[Ww]rites[[:space:]]*:[[:space:]]*//')
    for p in $(echo "$w" | tr ',' ' '); do
      [ -n "$p" ] && echo "$p $(basename "$f")" >> "$tmp"
    done
  done

  dups=$(awk '{print $1}' "$tmp" | sort | uniq -d)
  if [ -n "$dups" ]; then
    while IFS= read -r d; do
      [ -z "$d" ] && continue
      owners=$(awk -v p="$d" '$1==p {print $2}' "$tmp" | tr '\n' ' ')
      echo "FAIL FM-13: path '$d' claimed by multiple tasks in $(basename "$wave_dir"): $owners"
      fail=1
    done <<< "$dups"
  fi
  rm -f "$tmp"
done

[ "$fail" -eq 0 ] && echo "OK FM-13: task writes disjoint (static check)"
exit $fail
