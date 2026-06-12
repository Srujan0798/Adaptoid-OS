#!/usr/bin/env bash
# Validator test suite
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$HERE/.."
rc=0

echo "=== Validator Tests ==="

# Test: dogfood passes
echo "Test: dogfood.sh"
bash "$ROOT/validators/dogfood.sh" || rc=1

# Test: preflight passes
echo "Test: preflight.sh"
bash "$ROOT/validators/preflight.sh" "$ROOT" || rc=1

# Test: route_sentinel on missing config (should skip gracefully)
echo "Test: route_sentinel.sh (no config)"
bash "$ROOT/validators/route_sentinel.sh" "$ROOT" || rc=1

# Test: vault_mmu on missing memory (should skip gracefully)
echo "Test: vault_mmu.sh (no memory)"
bash "$ROOT/validators/vault_mmu.sh" "$ROOT" || rc=1

# Test: oap_security on missing policies (should warn gracefully)
echo "Test: oap_security.sh (no policies)"
bash "$ROOT/validators/oap_security.sh" "$ROOT" || rc=1

# Test: check_intent on missing intent (should skip gracefully)
echo "Test: check_intent.sh (no intent)"
bash "$ROOT/validators/check_intent.sh" "$ROOT" || rc=1

# Test: audit_chain on missing events (should skip gracefully)
echo "Test: audit_chain.sh (no events)"
bash "$ROOT/validators/audit_chain.sh" "$ROOT" || rc=1

# Test: engine smoke test
echo "Test: engine.py smoke"
TMPDIR=$(mktemp -d)
python3 "$ROOT/adaptor/engine.py" --brief "test cli tool" --output "$TMPDIR/test-project" --skip-verify >/dev/null 2>&1
if [ -d "$TMPDIR/test-project/orchestrator/scripts" ]; then
  echo "  PASS: engine generates structure"
else
  echo "  FAIL: engine did not generate structure"
  rc=1
fi
rm -rf "$TMPDIR"

# Test: Super-Adaptoid protocol validators (v5.0)
echo "Test: super-adaptoid validators"
for v in check_consciousness check_memory_identity check_evolution check_proactive_assistant \
         check_hidden_gems check_fable5 check_super_prompt; do
  bash "$ROOT/validators/$v.sh" "$ROOT" || rc=1
done

echo ""
if [ "$rc" -eq 0 ]; then
  echo "ALL TESTS PASS ✅"
else
  echo "SOME TESTS FAIL ❌"
fi
exit $rc
