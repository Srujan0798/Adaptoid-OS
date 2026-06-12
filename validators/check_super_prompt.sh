#!/usr/bin/env bash
# check_super_prompt.sh — Validates the Super-Prompt protocol (versioned, tested prompts).
# Usage: check_super_prompt.sh [repo_root]
set -uo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/super-prompt.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL super-prompt: $PROTO not found"; exit 1; }

for var in trigger_protocols PROJECT_INTENT confidence_threshold irreversible_threshold task_description; do
  grep -q "{{$var}}" "$PROTO" || { echo "FAIL super-prompt: missing template variable '{{$var}}'"; fail=1; }
done

for kfile in PRINCIPLES.md TWO-TIER.md ANTI-HALLUCINATION.md; do
  grep -q "$kfile" "$PROTO" || { echo "FAIL super-prompt: missing kernel reference '$kfile'"; fail=1; }
done

grep -qi "versioning" "$PROTO" || { echo "FAIL super-prompt: missing versioning ritual"; fail=1; }

[ "$fail" -eq 0 ] && echo "OK  super-prompt protocol valid"
exit "$fail"
