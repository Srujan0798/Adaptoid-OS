#!/usr/bin/env bash
# Kick a research wave note. Agents fill content; this only scaffolds.
# Usage: bash docs/research/era-ocean/scripts/wave_runner.sh [focus-slug]
set -euo pipefail
# scripts/ → era-ocean/ → research/ → docs/ → repo root
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
OCEAN="$ROOT/docs/research/era-ocean"
TS=$(date -u +%Y%m%d-%H%M)
FOCUS="${1:-general}"
OUT="$OCEAN/waves/wave-${TS}-${FOCUS}.md"

mkdir -p "$OCEAN/waves"

cat > "$OUT" <<EOF
# Research wave — ${TS} — ${FOCUS}

> Status: **INCOMPLETE** · Coverage of agentic world: still ≪1%  
> Do not treat this wave as exhaustive.

## Focus
${FOCUS}

## Sources hit
- (agent fills)

## Concepts extracted
- (agent fills)

## Elite candidates (for ELITE-10-PERCENT.md)
- (agent fills)

## Adaptoid delta (adopt / watch / refuse)
| Concept | Verdict | Target file if adopt |
|---|---|---|
| | | |

## Gaps opened (ocean grew)
- (agent fills)

## Next wave should hit
- (agent fills)
EOF

echo "Wrote $OUT"
{
  echo "| ${TS} | ${FOCUS} | \`${OUT#$ROOT/}\` |"
} >> "$OCEAN/MANIFEST.md"
echo "Manifest updated."
