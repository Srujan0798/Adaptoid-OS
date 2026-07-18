#!/usr/bin/env bash
# Adaptoid OS — One-Command Installer
set -euo pipefail

REPO_URL="https://github.com/Srujan0798/Adaptoid-OS.git"
INSTALL_DIR="${1:-$HOME/adaptoid-os}"

echo "⚡ Installing Adaptoid OS (Lite + Core)..."

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
VER="5.3.0"
[ -f "$INSTALL_DIR/VERSION" ] && VER="$(tr -d '[:space:]' < "$INSTALL_DIR/VERSION")"
echo "✅ Adaptoid OS v${VER} installed at $INSTALL_DIR"
echo ""
echo "Two surfaces:"
echo "  Lite  — ADAPTOID-LITE.md   (paste into any chat + brief)"
echo "  Core  — this whole folder  (engine --core-only --host all)"
echo ""
echo "Next steps:"
echo "  cd $INSTALL_DIR"
echo "  # Lite: open ADAPTOID-LITE.md, paste into agent + brief"
echo "  # Core:"
echo "  python3 adaptor/engine.py \\"
echo "    --brief 'Your project idea' \\"
echo "    --output ./my-project \\"
echo "    --core-only \\"
echo "    --host all"
echo ""
echo "  make ship-check   # full product gate"
echo "  See USE.md · FLOW.md · PRODUCT.md"
