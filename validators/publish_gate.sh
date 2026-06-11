#!/usr/bin/env bash
# FM-07 — Embarrassing artifacts / secrets. Blocks before commit/push.
# Usage: publish_gate.sh [project_root] [--fix] [--dry-run]
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

# 1. Forbidden filenames
bad_names=$(find "$ROOT" -type f \
  -not -path '*/.git/*' -not -path '*/node_modules/*' -not -path '*/attic/*' -not -path '*/scratch/*' \
  -not -path '*/venv/*' -not -path '*/.venv/*' -not -path '*/site-packages/*' \
  -not -path '*/dist/*' -not -path '*/build/*' -not -path '*/.mypy_cache/*' \
  \( -iname '*cheat*sheet*' -o -iname '*cheatsheet*' -o -iname '*defense*guide*' \
     -o -iname '*defence*guide*' -o -iname 'ORC_PROMPT*' -o -iname '*_REVIEW_PROMPT*' \
     -o -iname '*review_simulator*' -o -iname '*professor_review*' -o -iname 'session-ses*' \
     -o -iname 'kimi-export*' -o -iname '*MEETING_CHEAT*' \) 2>/dev/null)

if [ -n "$bad_names" ]; then
  echo "FAIL FM-07: embarrassing artifact filenames present:"; echo "$bad_names" | sed 's/^/  /'
  if [ "$FIX" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would move artifacts to attic/"
    else
      mkdir -p "$ROOT/attic"
      echo "$bad_names" | while IFS= read -r f; do
        mv "$f" "$ROOT/attic/$(basename "$f")"
        echo "  FIXED: moved $(basename "$f") → attic/"
      done
    fi
  fi
  fail=1
fi

# 2. Secret-ish content
secrets=$(grep -rInE \
  '(AKIA[0-9A-Z]{16}|-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY|sk-[A-Za-z0-9]{20,}|xox[baprs]-[0-9A-Za-z-]+)' \
  "$ROOT" --include='*.py' --include='*.ts' --include='*.js' --include='*.env*' --include='*.yaml' --include='*.yml' --include='*.md' \
  --exclude-dir=venv --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=site-packages \
  --exclude-dir=.git --exclude-dir=dist --exclude-dir=build \
  2>/dev/null | grep -v '.env.example' || true)
if [ -n "$secrets" ]; then
  echo "FAIL FM-07: possible secret(s) detected:"; echo "$secrets" | sed 's/^/  /'
  fail=1
fi

# 3. Tracked .env
if [ -d "$ROOT/.git" ]; then
  if git -C "$ROOT" ls-files --error-unmatch .env >/dev/null 2>&1; then
    echo "FAIL FM-07: .env is tracked by git — add to .gitignore and untrack."
    if [ "$FIX" -eq 1 ] && [ "$DRY" -eq 0 ]; then
      git -C "$ROOT" rm --cached .env 2>/dev/null || true
      echo ".env" >> "$ROOT/.gitignore"
      echo "  FIXED: untracked .env and added to .gitignore"
    elif [ "$FIX" -eq 1 ]; then
      echo "  [DRY-RUN] would untrack .env and add to .gitignore"
    fi
    fail=1
  fi
fi

[ "$fail" -eq 0 ] && echo "OK FM-07: no embarrassing artifacts or secrets found"
exit $fail
