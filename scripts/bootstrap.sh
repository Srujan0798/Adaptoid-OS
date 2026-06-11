#!/usr/bin/env bash
# Adaptoid OS — Project Bootstrap
# Usage: bootstrap.sh <project_name> [--archetype <type>] [--tier <T0-T4>] [--output <dir>]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_NAME="${1:-my-project}"
ARCHETYPE="internal-tool"
TIER="T1"
OUTPUT_DIR="."
shift || true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --archetype) ARCHETYPE="$2"; shift 2 ;;
    --tier) TIER="$2"; shift 2 ;;
    --output) OUTPUT_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

TARGET="$OUTPUT_DIR/$PROJECT_NAME"
echo "⚡ Bootstrapping $PROJECT_NAME ($ARCHETYPE @ $TIER)..."

mkdir -p "$TARGET"
cp -r "$SCRIPT_DIR/templates/root/"* "$TARGET/"
cp -r "$SCRIPT_DIR/templates/orchestrator/"* "$TARGET/orchestrator/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/work/"* "$TARGET/work/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/plan/"* "$TARGET/plan/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/specify/"* "$TARGET/specify/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/docs/"* "$TARGET/docs/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/evals/"* "$TARGET/evals/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/templates/ci/"* "$TARGET/.github/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/validators/"* "$TARGET/orchestrator/scripts/"

# Fill placeholders
find "$TARGET" -type f -name '*.md' -o -name '*.yaml' -o -name '*.yml' | while read -r f; do
  sed -i.bak "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$f"
  sed -i.bak "s/{{ARCHETYPE}}/$ARCHETYPE/g" "$f"
  sed -i.bak "s/{{TIER}}/$TIER/g" "$f"
  sed -i.bak "s/{{DATE}}/$(date +%Y-%m-%d)/g" "$f"
  rm -f "$f.bak"
done

echo "🔍 Running preflight..."
cd "$TARGET" && bash orchestrator/scripts/preflight.sh . || true

echo "✅ $PROJECT_NAME ready at $TARGET"
echo "Next: paste your brief into PROJECT-INTENT.md and run 'bash orchestrator/scripts/preflight.sh'"
