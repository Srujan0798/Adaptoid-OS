#!/usr/bin/env bash
# Adaptoid OS — Health Check
# Usage: healthcheck.sh [project_root]
set -uo pipefail
ROOT="${1:-.}"

echo "=== Adaptoid OS Health Check ==="
echo ""

# Check core files
for f in kernel/PRINCIPLES.md kernel/TWO-TIER.md kernel/ANTI-HALLUCINATION.md INDEX.md validators/dogfood.sh validators/preflight.sh; do
  if [ -f "$ROOT/$f" ]; then
    echo "✅ $f"
  else
    echo "❌ $f MISSING"
  fi
done

echo ""
echo "=== Validators ==="
find "$ROOT/validators" -name '*.sh' -executable | wc -l | xargs echo "Executable validators:"

echo ""
echo "=== Dogfood ==="
cd "$ROOT" && bash validators/dogfood.sh

echo ""
echo "=== Preflight ==="
cd "$ROOT" && bash validators/preflight.sh .
