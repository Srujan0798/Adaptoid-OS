#!/usr/bin/env bash
# FM-03 — Broken references. Fails on markdown links to missing local files.
# Usage: check_references.sh [project_root] [--fix] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"
FIX=0
DRY=0
shift || true

for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    --dry-run) DRY=1 ;;
  esac
done

fail=0

while IFS= read -r md; do
  grep -oE '\]\(([^)]+)\)' "$md" 2>/dev/null | sed -E 's/^\]\(|\)$//g' | while IFS= read -r link; do
    case "$link" in
      http*|mailto:*|\#*) continue ;;
    esac
    target="${link%%#*}"
    [ -z "$target" ] && continue
    case "$target" in
      */*) : ;;
      *.*) : ;;
      *) continue ;;
    esac
    dir=$(dirname "$md")
    if [ ! -e "$dir/$target" ] && [ ! -e "$ROOT/$target" ]; then
      echo "FAIL FM-03: $md → missing '$target'"
      if [ "$FIX" -eq 1 ]; then
        if [ "$DRY" -eq 1 ]; then
          echo "  [DRY-RUN] would comment out or mark broken link"
        else
          # Comment out the broken link in place
          sed -i.bak "s|\]($link)|]($link) <!-- BROKEN: run check_references.sh -->|g" "$md"
          rm -f "$md.bak"
          echo "  FIXED: marked broken link in $md"
        fi
      fi
      echo "x" >> /tmp/.fm03_$$
    fi
  done
# Vendored skill/plugin docs are third-party content whose examples are
# illustrative, not paths in this repo — e.g. `./src/ordering/CONTEXT.md` in a
# domain-modeling skill, or a dated playwright trace filename. FM-03 is about
# *this project's* docs pointing at things that do not exist; holding vendored
# material to that standard produces failures nobody in the repo can fix.
done < <(find "$ROOT" -name '*.md' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' -not -path '*/attic/*' \
  -not -path '*/.agents/skills/*' -not -path '*/.claude/skills/*' \
  -not -path '*/.claude/plugins/*' 2>/dev/null)

if [ -f /tmp/.fm03_$$ ]; then fail=1; rm -f /tmp/.fm03_$$; fi
[ "$fail" -eq 0 ] && echo "OK FM-03: all markdown references resolve"
exit $fail
