#!/usr/bin/env bash
# FM-11 — Silent failures. Flags swallowed exceptions and bare fallbacks.
# Usage: check_silent_failures.sh [project_root] [--fix] [--dry-run]
# Note: --fix only comments out bare excepts; swallowed excepts need human review.
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

# bare/swallowing excepts (Python)
swallow=$(grep -rInE 'except[^:]*:\s*(pass|\.\.\.)\s*$' "$ROOT/src" 2>/dev/null || true)
bare=$(grep -rInE '^\s*except\s*:' "$ROOT/src" 2>/dev/null || true)
if [ -n "$swallow$bare" ]; then
  echo "FAIL FM-11: swallowed/bare exception(s):"
  [ -n "$swallow" ] && echo "$swallow" | sed 's/^/  /'
  [ -n "$bare" ] && echo "$bare" | sed 's/^/  /'
  echo "  → catch specific exceptions; log or re-raise; never silently pass."
  if [ "$FIX" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would comment out bare except: blocks (requires human review)"
    else
      # Comment out bare except: lines (destructive — use with care)
      find "$ROOT/src" -name '*.py' -exec sed -i.bak -E '/^\s*except\s*:\s*$/c\    except Exception as e:  # TODO: catch specific; log or re-raise' {} + 2>/dev/null || true
      find "$ROOT/src" -name '*.py.bak' -delete 2>/dev/null || true
      echo "  FIXED: replaced bare except: with except Exception as e: (review needed)"
    fi
  fi
  fail=1
fi

# JS/TS empty catch
jscatch=$(grep -rInE 'catch\s*\([^)]*\)\s*\{\s*\}' "$ROOT/src" 2>/dev/null || true)
if [ -n "$jscatch" ]; then
  echo "FAIL FM-11: empty catch block(s):"; echo "$jscatch" | sed 's/^/  /'
  fail=1
fi

[ "$fail" -eq 0 ] && echo "OK FM-11: no obvious silent failures"
exit $fail
