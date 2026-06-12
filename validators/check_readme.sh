#!/usr/bin/env bash
# validators/check_readme.sh
# Checks README.md against a 10-point open-source README heuristic.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
README="$ROOT/README.md"
fail=0

echo "[CHECK] README exists..."
[ -f "$README" ] || { echo "FAIL: README.md not found"; exit 1; }

# 1. Clear one-sentence description in first 100 words
FIRST100=$(head -c 500 "$README" | wc -w | awk '{print $1}')
if ! head -c 500 "$README" | grep -qiE "harness|framework|operating system|agent"; then
  echo "FAIL: no one-sentence description in first ~100 words"
  fail=1
else
  echo "OK: one-sentence description present"
fi

# 2. Problem stated in one paragraph
if ! grep -q "## The Problem" "$README"; then
  echo "FAIL: missing '## The Problem' section"
  fail=1
else
  echo "OK: problem section present"
fi

# 3. Comparison matrix or differentiator
if ! grep -q "## Why Adaptoid OS Wins" "$README"; then
  echo "FAIL: missing comparison / differentiator section"
  fail=1
else
  echo "OK: comparison section present"
fi

# 4. 30-second quick start
if ! grep -q "## Quick Start" "$README"; then
  echo "FAIL: missing '## Quick Start' section"
  fail=1
else
  echo "OK: quick start section present"
fi

# 5. Key features with evidence
if ! grep -q "## Features" "$README"; then
  echo "FAIL: missing '## Features' section"
  fail=1
else
  echo "OK: features section present"
fi

# 6. Architecture docs linked
if ! grep -q "## Architecture" "$README"; then
  echo "FAIL: missing '## Architecture' section"
  fail=1
else
  echo "OK: architecture section present"
fi

# 7. Contributing linked
if ! grep -qi "contributing" "$README"; then
  echo "FAIL: missing contributing reference"
  fail=1
else
  echo "OK: contributing reference present"
fi

# 8. License displayed
if ! grep -qi "license" "$README"; then
  echo "FAIL: missing license reference"
  fail=1
else
  echo "OK: license reference present"
fi

# 9. CTA present
if ! grep -q "⭐ Star" "$README"; then
  echo "FAIL: missing CTA (star / try / contribute)"
  fail=1
else
  echo "OK: CTA present"
fi

# 10. No hype / copyrighted terms
HYPE=$(grep -inE "battle-tested|groundbreaking|revolutionary|#1|best in class|market leader" "$README" || true)
# Flag standalone "Super-Adaptoid" (not inside a protocols/super-adaptoid/ file path)
COPY=$(grep -in "Super-Adaptoid" "$README" | grep -vE 'protocols/super-adaptoid|super-adaptoid/' || true)
if [ -n "$HYPE" ]; then
  echo "FAIL: hype language found:"
  echo "$HYPE"
  fail=1
fi
if [ -n "$COPY" ]; then
  echo "FAIL: copyrighted standalone terms found:"
  echo "$COPY"
  fail=1
fi
if [ -z "$HYPE" ] && [ -z "$COPY" ]; then
  echo "OK: no hype or copyrighted standalone terms"
fi

[ "$fail" -eq 0 ] && echo "OK  README passes 10-point heuristic"
exit "$fail"
