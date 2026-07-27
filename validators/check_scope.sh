#!/usr/bin/env bash
# FM-08 — Scope creep / over-building.
# Flags undeclared top-level files/dirs and missing SCOPE_GUARD.md.
# Usage: check_scope.sh [project_root] [--fix] [--dry-run]
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

# SCOPE_GUARD.md should exist for non-trivial projects
if [ ! -f "$ROOT/docs/SCOPE_GUARD.md" ] && [ ! -f "$ROOT/SCOPE_GUARD.md" ]; then
  echo "WARN FM-08: no SCOPE_GUARD.md found (IN/OUT/LATER scope not declared)"
  # Not a hard fail; many small projects start without one
fi

# HIERARCHY.md declares allowed top-level files/dirs
HIERARCHY="$ROOT/HIERARCHY.md"
if [ -f "$HIERARCHY" ]; then
  # Collect declared top-level entries (first-level headers, bullets, or backtick names)
  declared=$(grep -oE '^[-*] `[^`]+`|^## `[^`]+`|^`[^`]+`' "$HIERARCHY" 2>/dev/null | sed 's/^ *[-*#]* *//; s/ *$//; s/`//g; s|/$||' | sort -u)
  if [ -n "$declared" ]; then
    while IFS= read -r entry; do
      [ -z "$entry" ] && continue
      # Check if a matching top-level file/dir exists and is not declared
      for top in "$ROOT/$entry" "$ROOT/${entry%/}"; do
        if [ -e "$top" ]; then
          base=$(basename "$top")
          if ! echo "$declared" | grep -qx "$base"; then
            echo "FAIL FM-08: top-level '$base' not declared in HIERARCHY.md"
            fail=1
          fi
        fi
      done
    done < <(ls -1 "$ROOT" | grep -vE '^\.')
  fi
fi

# Check worker reports for files touched outside the brief's declared list
REPORTS_DIR="$ROOT/work/reports"
if [ -d "$REPORTS_DIR" ]; then
  while IFS= read -r report; do
    brief_files=$(grep -oE '`[^`]+`' "$report" 2>/dev/null | tr -d '`' | grep -E '\.(md|py|js|ts|tsx|jsx|go|rs|java|sh|yaml|json|toml)$' | sort -u)
    changed=$(grep -iE '^[-*] changed|^[-*] modified|^[-*] touched|^[-*] files?' "$report" 2>/dev/null | sed -E 's/^[-*:] +//' | grep -oE '[A-Za-z0-9_./-]+\.[A-Za-z0-9]+' | sort -u)
    if [ -n "$brief_files" ] && [ -n "$changed" ]; then
      extras=$(comm -23 <(echo "$changed") <(echo "$brief_files"))
      if [ -n "$extras" ]; then
        echo "FAIL FM-08: $report touches files outside the brief:"
        echo "$extras" | sed 's/^/  /'
        fail=1
      fi
    fi
  done < <(find "$REPORTS_DIR" -name '*.md' 2>/dev/null)
fi

[ "$fail" -eq 0 ] && echo "OK FM-08: scope guard clean"
exit $fail
