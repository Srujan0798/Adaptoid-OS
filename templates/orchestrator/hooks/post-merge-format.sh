#!/usr/bin/env bash
# Post-merge hook — run validators after merging worker output.
# Usage: bash orchestrator/hooks/post-merge-format.sh [project_root]
set -uo pipefail
ROOT="${1:-.}"

echo "=== Post-merge validation ==="
bash "$ROOT/orchestrator/scripts/preflight.sh" "$ROOT"
rc=$?

if [ "$rc" -eq 0 ]; then
  echo "=== Regenerating derived docs (FM-12) ==="
  # Add your derived-doc regeneration commands here
  # e.g. python scripts/generate_readme.py
fi

exit $rc
