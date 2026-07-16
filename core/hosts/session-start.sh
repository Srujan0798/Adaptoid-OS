#!/usr/bin/env bash
# Adaptoid Core — Claude Code SessionStart hook (optional).
# Prints orientation paths; does not mutate project state.
set -euo pipefail
ROOT="${CLAUDE_PROJECT_DIR:-.}"
echo "[adaptoid] Session start — orient on:"
echo "  $ROOT/kernel/PRINCIPLES.md"
echo "  $ROOT/HANDOFF.md"
echo "  $ROOT/PROJECT-INTENT.md"
echo "  $ROOT/adaptoid.config.yaml"
if [ -f "$ROOT/HANDOFF.md" ]; then
  echo "[adaptoid] HANDOFF present"
else
  echo "[adaptoid] WARN: HANDOFF.md missing (FM-14)"
fi
