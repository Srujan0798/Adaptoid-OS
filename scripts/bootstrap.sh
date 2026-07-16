#!/usr/bin/env bash
# Adaptoid OS — Project Bootstrap
# Usage:
#   bootstrap.sh <project_name> [--archetype <type>] [--tier <T0-T4>]
#               [--output <dir>] [--host <agents,claude,...|all>] [--core-only]
#               [--brief "text"]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_NAME="${1:-my-project}"
ARCHETYPE=""
TIER=""
OUTPUT_DIR="."
HOST="agents,claude"
CORE_ONLY=0
BRIEF=""
shift || true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --archetype) ARCHETYPE="$2"; shift 2 ;;
    --tier) TIER="$2"; shift 2 ;;
    --output) OUTPUT_DIR="$2"; shift 2 ;;
    --host) HOST="$2"; shift 2 ;;
    --core-only) CORE_ONLY=1; shift ;;
    --brief) BRIEF="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

TARGET="$OUTPUT_DIR/$PROJECT_NAME"
if [[ -z "$BRIEF" ]]; then
  BRIEF="Project $PROJECT_NAME"
  if [[ -n "$ARCHETYPE" ]]; then
    BRIEF="$BRIEF ($ARCHETYPE)"
  fi
fi

echo "⚡ Bootstrapping $PROJECT_NAME via Adaptoid engine..."
echo "   host=$HOST  core_only=$CORE_ONLY  output=$TARGET"

ENGINE_ARGS=(
  --brief "$BRIEF"
  --output "$TARGET"
  --host "$HOST"
)
if [[ -n "$ARCHETYPE" ]]; then
  ENGINE_ARGS+=(--archetype "$ARCHETYPE")
fi
if [[ -n "$TIER" ]]; then
  ENGINE_ARGS+=(--tier "$TIER")
fi
if [[ "$CORE_ONLY" -eq 1 ]]; then
  ENGINE_ARGS+=(--core-only)
fi

python3 "$SCRIPT_DIR/adaptor/engine.py" "${ENGINE_ARGS[@]}"

echo ""
echo "✅ $PROJECT_NAME ready at $TARGET"
echo "Next:"
echo "  1. Edit $TARGET/PROJECT-INTENT.md"
echo "  2. Open your host agent in $TARGET"
echo "  3. bash $TARGET/orchestrator/scripts/preflight.sh $TARGET"
