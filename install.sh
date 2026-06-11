#!/usr/bin/env bash
# Adaptoid OS — One-Command Installer
set -euo pipefail

REPO_URL="https://github.com/YOUR_USERNAME/adaptoid-os.git"
INSTALL_DIR="${1:-$HOME/adaptoid-os}"

echo "⚡ Installing Adaptoid OS v4.0..."

if [ -d "$INSTALL_DIR" ]; then
  echo "Directory $INSTALL_DIR already exists. Updating..."
  cd "$INSTALL_DIR"
  git pull origin main || true
else
  git clone "$REPO_URL" "$INSTALL_DIR"
  cd "$INSTALL_DIR"
fi

echo "🔍 Running dogfood validation..."
bash validators/dogfood.sh

echo "✅ Adaptoid OS installed at $INSTALL_DIR"
echo ""
echo "Next steps:"
echo "  cd $INSTALL_DIR"
echo "  python3 adaptor/engine.py --brief 'Your project idea' --output ./my-project"
echo ""
echo "Or paste 00-INVOCATION.md into Claude Code / Kimi and start shipping."
