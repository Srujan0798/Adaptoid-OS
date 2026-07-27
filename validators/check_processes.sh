#!/usr/bin/env bash
# FM-02 — Stale process with wrong params.
# Refuses to greenlight a new long run if one is already alive for this project.
# Usage: check_processes.sh <project_marker> [expected_param=value ...] [--fix] [--dry-run]
set -uo pipefail
MARKER="${1:-$(basename "$PWD")}"
shift || true

FIX=0
DRY=0
params=()

for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    --dry-run) DRY=1 ;;
    *=*) params+=("$arg") ;;
  esac
done

# FM-02 is about long-running jobs (training, serving) left alive with stale
# params — not about transient tooling. `git`, `hook` and `pre-commit` are
# excluded because this validator runs *inside* a pre-commit hook: without
# them it detects its own parent `git -C <project> commit` as a stale run and
# fails every commit, permanently. Found on first live use, 2026-07-27.
hits=$(ps aux | grep -iE "$MARKER" | grep -viE "grep|Cursor Helper|Code Helper|check_processes|check_tests|check_|preflight|emit_event|opencode|claude |bash|zsh|ps aux|node |npm |git |hook|pre-commit" || true)

if [ -n "$hits" ]; then
  echo "WARN FM-02: existing process(es) matching '$MARKER' are running:"
  echo "$hits" | awk '{printf "  PID %s  %s\n", $2, substr($0, index($0,$11))}'

  # Param mismatch check
  param_drift=0
  for kv in ${params[@]+"${params[@]}"}; do
    key="${kv%%=*}"; val="${kv##*=}"
    running=$(echo "$hits" | grep -oE -- "--?${key}[ =][^ ]+" | head -1)
    if [ -n "$running" ] && ! echo "$running" | grep -q "$val"; then
      echo "  ✗ param drift: running '$running' but expected $key=$val"
      param_drift=1
    fi
  done

  if [ "$param_drift" -eq 1 ] && [ "$FIX" -eq 1 ]; then
    pids=$(echo "$hits" | awk '{print $2}')
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would kill PIDs: $pids"
    else
      echo "$hits" | awk '{print $2}' | xargs kill 2>/dev/null || true
      echo "  FIXED: killed stale processes with param drift"
    fi
  fi

  echo "FAIL FM-02: kill the stale run (or confirm it's intended) before starting a new one."
  exit 1
fi
echo "OK FM-02: no conflicting process for '$MARKER'"
exit 0
