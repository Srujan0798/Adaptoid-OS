#!/usr/bin/env bash
# Session start hook — validate context before the orchestrator begins.
# Usage: bash orchestrator/hooks/session-start.sh [project_root]
set -uo pipefail
ROOT="${1:-.}"

echo "=== Session start: validating context ==="

# 1. Kernel must exist
for f in kernel/PRINCIPLES.md kernel/TWO-TIER.md kernel/ANTI-HALLUCINATION.md; do
  if [ ! -f "$ROOT/$f" ]; then
    echo "MISSING KERNEL: $f — this project may not be OS-Setup compliant"
    exit 1
  fi
done

# 2. State files must be consistent
bash "$ROOT/orchestrator/scripts/validate_state.sh" "$ROOT"

# 3. Context budget check
bash "$ROOT/orchestrator/scripts/context_budget.sh" "$ROOT"

# 4. No stale processes
bash "$ROOT/orchestrator/scripts/check_processes.sh" "$(basename "$ROOT")"

# 5. Config lock match (if exists)
[ -d "$ROOT/configs" ] && bash "$ROOT/orchestrator/scripts/check_config.sh" "$ROOT"

echo "=== Session start: OK ==="
