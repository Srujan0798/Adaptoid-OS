#!/usr/bin/env bash
# wake.sh — Session crash recovery. Rebuilds context from durable files.
# Usage: wake.sh [wave] [task]
set -uo pipefail

ROOT="${1:-.}"
WAVE="${2:-}"
TASK="${3:-}"

echo "=== WAKE: Rebuilding orchestrator context ==="
echo ""

# 1. Kernel (always)
for f in kernel/PRINCIPLES.md kernel/TWO-TIER.md kernel/ANTI-HALLUCINATION.md; do
  if [ -f "$ROOT/$f" ]; then
    echo "✓ $f"
  else
    echo "✗ MISSING: $f — this project may not be OS-Setup compliant"
  fi
done
echo ""

# 2. HANDOFF.md (current state)
if [ -f "$ROOT/HANDOFF.md" ]; then
  echo "✓ HANDOFF.md — last updated: $(stat -f %Sm "$ROOT/HANDOFF.md" 2>/dev/null || stat -c %y "$ROOT/HANDOFF.md" 2>/dev/null)"
  ACTIVE=$(grep -ioE 'active wave[^0-9]*[0-9]+' "$ROOT/HANDOFF.md" | grep -oE '[0-9]+' | head -1)
  [ -n "$ACTIVE" ] && echo "  Active wave: wave-$ACTIVE"
else
  echo "✗ MISSING: HANDOFF.md — no session state available"
fi
echo ""

# 3. EXECUTION.md (shipped waves)
if [ -f "$ROOT/plan/EXECUTION.md" ]; then
  SHIPPED=$(grep -c "SHIPPED" "$ROOT/plan/EXECUTION.md" 2>/dev/null || echo 0)
  echo "✓ EXECUTION.md — $SHIPPED wave(s) shipped"
else
  echo "✗ MISSING: plan/EXECUTION.md"
fi
echo ""

# 4. Session events (if wave/task given)
if [ -n "$WAVE" ] && [ -n "$TASK" ]; then
  EVENT_FILE="$ROOT/orchestrator/memory/session/${WAVE}-${TASK}.events.jsonl"
  if [ -f "$EVENT_FILE" ]; then
    echo "✓ Session log: ${WAVE}-${TASK}.events.jsonl ($(wc -l < "$EVENT_FILE" | tr -d ' ') events)"
    bash "$ROOT/validators/replay_session.sh" "$WAVE" "$TASK" 5 2>/dev/null || true
  else
    echo "✗ No session log for $WAVE / $TASK"
  fi
  echo ""
fi

# 5. Config
if [ -f "$ROOT/adaptoid.config.yaml" ]; then
  echo "✓ adaptoid.config.yaml — project config present"
else
  echo "⚠ adaptoid.config.yaml missing — consider adding for single-source-of-truth"
fi
echo ""

# 6. Quick health check
if [ -x "$ROOT/validators/preflight.sh" ]; then
  echo "Running quick preflight (subset)..."
  bash "$ROOT/validators/preflight.sh" "$ROOT" 2>/dev/null | tail -n 5
fi

echo ""
echo "=== WAKE complete. Context rebuilt. Proceed with next phase. ==="
