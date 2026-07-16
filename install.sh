#!/usr/bin/env bash
# Adaptoid OS — One-Command Installer (v5.1 Core/Pro)
set -euo pipefail

REPO_URL="https://github.com/Srujan0798/Adaptoid-OS.git"
INSTALL_DIR="${1:-$HOME/adaptoid-os}"

echo "⚡ Installing Adaptoid OS v5.1 (Core + Pro kit)..."

if [ -d "$INSTALL_DIR/.git" ]; then
  echo "Directory $INSTALL_DIR already exists. Updating..."
  cd "$INSTALL_DIR"
  git pull origin main || true
elif [ -d "$INSTALL_DIR" ]; then
  echo "Directory $INSTALL_DIR exists but is not a git clone. Using as-is."
  cd "$INSTALL_DIR"
else
  git clone "$REPO_URL" "$INSTALL_DIR"
  cd "$INSTALL_DIR"
fi

echo "🔍 Running dogfood validation..."
bash validators/dogfood.sh

echo ""
echo "✅ Adaptoid OS installed at $INSTALL_DIR"
echo ""
echo "Product ladder:"
echo "  Lite  — reference/OS_SETUP_v1.3_full.md  (paste into any chat)"
echo "  Core  — engine --core-only --host all     (default for real projects)"
echo "  Pro   — this full repository"
echo ""
echo "Next steps:"
echo "  cd $INSTALL_DIR"
echo "  python3 adaptor/engine.py \\"
echo "    --brief 'Your project idea' \\"
echo "    --output ./my-project \\"
echo "    --core-only \\"
echo "    --host all"
echo ""
echo "  python3 conductor/conductor.py wake --project ./my-project"
echo "  make ship-check   # full product gate"
echo ""
echo "Or paste 00-INVOCATION.md into your coding agent and start shipping."
