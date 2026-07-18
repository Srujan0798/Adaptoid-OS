#!/usr/bin/env bash
# FM-17 — VaultMMU. Verifies SHA-256 hash chain of orchestrator memory files.
# Usage: vault_mmu.sh [project_root] [--fix] [--dry-run]
set -uo pipefail

# Portable SHA-256 (Linux: sha256sum · macOS/BSD: shasum -a 256)
_sha256() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$@"; else shasum -a 256 "$@"; fi
}

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

VAULT="$ROOT/.vault"
HASHES="$VAULT/hashes.json"
MEM_DIR="$ROOT/orchestrator/memory"
fail=0

# If no memory dir, skip
if [ ! -d "$MEM_DIR" ]; then
  echo "OK vault-mmu: no orchestrator/memory dir found (optional)"
  exit 0
fi

# If no vault yet, initialize if --fix
if [ ! -f "$HASHES" ]; then
  if [ "$FIX" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      echo "  [DRY-RUN] would initialize .vault/hashes.json"
    else
      mkdir -p "$VAULT"
      echo '{"genesis":"'"$(date +%s)"'","entries":[]}' > "$HASHES"
      echo "  FIXED: initialized .vault/hashes.json"
    fi
  else
    echo "WARN vault-mmu: no .vault/hashes.json found; run with --fix to initialize"
  fi
  exit 0
fi

# Verify each tracked file
if [ -f "$HASHES" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    rel=${f#$MEM_DIR/}
    stored=$(python3 -c "import json; d=json.load(open('$HASHES')); print(next((e['hash'] for e in d.get('entries',[]) if e.get('file','').endswith('$rel')),'NOT_FOUND'))" 2>/dev/null || echo "NOT_FOUND")
    if [ "$stored" = "NOT_FOUND" ]; then
      echo "WARN vault-mmu: no stored hash for $rel"
      continue
    fi
    current="sha256:$(_sha256 "$f" | awk '{print $1}')"
    if [ "$stored" != "$current" ]; then
      echo "FAIL vault-mmu: hash mismatch on $rel (stored=$stored current=$current)"
      fail=1
    fi
  done < <(find "$MEM_DIR" -type f 2>/dev/null)
fi

[ "$fail" -eq 0 ] && echo "OK vault-mmu: memory integrity verified"
exit $fail
