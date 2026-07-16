#!/usr/bin/env bash
# check_memory_identity.sh — Validates the Memory-Identity protocol (4-tier durable memory).
# Usage: check_memory_identity.sh [repo_root]
set -euo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
PROTO="$ROOT/protocols/super-adaptoid/memory-identity.md"
fail=0

[ -f "$PROTO" ] || { echo "FAIL memory-identity: $PROTO not found"; exit 1; }

for tier in Working Episodic Semantic Identity; do
  grep -q "$tier" "$PROTO" || { echo "FAIL memory-identity: missing tier '$tier'"; fail=1; }
done

for field in enabled identity_card handoff_file memory_bank vault_dir hot_context_limit_tokens; do
  grep -q "$field" "$PROTO" || { echo "FAIL memory-identity: missing config field '$field'"; fail=1; }
done

for fm in FM-04 FM-06 FM-08 FM-18; do
  grep -q "$fm" "$PROTO" || { echo "FAIL memory-identity: missing failure mode '$fm'"; fail=1; }
done

[ "$fail" -eq 0 ] && echo "OK  memory-identity protocol valid"
exit "$fail"
