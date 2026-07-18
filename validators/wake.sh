#!/usr/bin/env bash
# wake.sh — Session crash recovery. Rebuilds context from durable files.
# Usage: wake.sh [project_root] [wave] [task]
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
    echo "✗ MISSING: $f — may not be an Adaptoid-generated project"
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

# 3. Intent + ship OS
for f in PROJECT-INTENT.md SHIP-SYSTEM.md HOST-OPERATING-PLAYBOOK.md AGENTS.md; do
  if [ -f "$ROOT/$f" ]; then
    echo "✓ $f"
  else
    echo "⚠ missing optional/cold-start: $f"
  fi
done
echo ""

# 4. Wave tasks (SDLC default layout)
if [ -d "$ROOT/work" ]; then
  n_tasks=$(find "$ROOT/work" -path '*/tasks/*.md' 2>/dev/null | wc -l | tr -d ' ')
  echo "✓ work/ present ($n_tasks task file(s))"
else
  echo "⚠ no work/ yet"
fi
if [ -f "$ROOT/plan/intent-lock.md" ]; then
  echo "✓ plan/intent-lock.md"
fi
if [ -f "$ROOT/plan/EXECUTION.md" ]; then
  SHIPPED=$(grep -c "SHIPPED" "$ROOT/plan/EXECUTION.md" 2>/dev/null || echo 0)
  echo "✓ plan/EXECUTION.md — $SHIPPED wave(s) shipped"
fi
echo ""

# 5. Session events (optional)
if [ -n "$WAVE" ] && [ -n "$TASK" ]; then
  EVENT_FILE="$ROOT/orchestrator/memory/session/${WAVE}-${TASK}.events.jsonl"
  if [ -f "$EVENT_FILE" ]; then
    echo "✓ Session log: ${WAVE}-${TASK}.events.jsonl ($(wc -l < "$EVENT_FILE" | tr -d ' ') events)"
  else
    echo "· No session log for $WAVE / $TASK (optional)"
  fi
  echo ""
fi

# 6. Config
if [ -f "$ROOT/adaptoid.config.yaml" ]; then
  echo "✓ adaptoid.config.yaml"
else
  echo "⚠ adaptoid.config.yaml missing"
fi
echo ""

# 7. Preflight — generated projects use orchestrator/scripts/
PREFLIGHT=""
if [ -x "$ROOT/orchestrator/scripts/preflight.sh" ] || [ -f "$ROOT/orchestrator/scripts/preflight.sh" ]; then
  PREFLIGHT="$ROOT/orchestrator/scripts/preflight.sh"
elif [ -x "$ROOT/validators/preflight.sh" ] || [ -f "$ROOT/validators/preflight.sh" ]; then
  PREFLIGHT="$ROOT/validators/preflight.sh"
fi
if [ -n "$PREFLIGHT" ]; then
  echo "Running preflight..."
  bash "$PREFLIGHT" "$ROOT" 2>/dev/null | tail -n 8
else
  echo "⚠ preflight.sh not found (orchestrator/scripts/ or validators/)"
fi

echo ""
echo "=== WAKE complete. Context rebuilt. Proceed with next phase. ==="
