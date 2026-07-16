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

# Test: Core + host emission integration
echo "Test: test_host_emit.py (Core + hosts)"
python3 "$ROOT/tests/test_host_emit.py" || rc=1

# Test: engine --core-only --host all produces host surfaces
echo "Test: engine core-only host all"
TMPDIR=$(mktemp -d)
python3 "$ROOT/adaptor/engine.py" \
  --brief "test cli tool" \
  --output "$TMPDIR/core-proj" \
  --core-only \
  --host all \
  --skip-verify >/dev/null 2>&1
ok=1
for f in AGENTS.md CLAUDE.md HANDOFF.md kernel/PRINCIPLES.md \
         .cursor/rules/adaptoid.mdc orchestrator/scripts/preflight.sh; do
  if [ ! -e "$TMPDIR/core-proj/$f" ]; then
    echo "  FAIL: missing $f"
    ok=0
    rc=1
  fi
done
[ "$ok" -eq 1 ] && echo "  PASS: core-only host all surfaces present"
rm -rf "$TMPDIR"

# Test: Super-Adaptoid protocol validators (v5.0)
echo "Test: super-adaptoid validators"
for v in check_consciousness check_memory_identity check_evolution check_proactive_assistant \
         check_hidden_gems check_fable5 check_super_prompt; do
  bash "$ROOT/validators/$v.sh" "$ROOT" || rc=1
done

# Test: Core package presence
echo "Test: core package present"
if [ -f "$ROOT/core/MANIFEST.yaml" ] && [ -f "$ROOT/core/README.md" ]; then
  echo "  PASS: core/ package present"
else
  echo "  FAIL: core/ package incomplete"
  rc=1
fi

# Test: conductor runtime
echo "Test: conductor.py"
TMPDIR=$(mktemp -d)
python3 "$ROOT/adaptor/engine.py" \
  --brief "test cli tool" \
  --output "$TMPDIR/cproj" \
  --core-only \
  --host agents \
  --skip-verify >/dev/null 2>&1
python3 "$ROOT/conductor/conductor.py" init-wave --project "$TMPDIR/cproj" --wave wave-1 -n 2 >/dev/null
python3 "$ROOT/conductor/conductor.py" check-disjoint --project "$TMPDIR/cproj" --wave wave-1 >/dev/null
python3 "$ROOT/conductor/conductor.py" dispatch --project "$TMPDIR/cproj" --wave wave-1 --mode stub >/dev/null
n_reports=$(find "$TMPDIR/cproj/work/reports" -name '*.report.md' 2>/dev/null | wc -l | tr -d ' ')
if [ "$n_reports" -ge 2 ]; then
  echo "  PASS: conductor init+dispatch ($n_reports reports)"
else
  echo "  FAIL: conductor reports=$n_reports"
  rc=1
fi
rm -rf "$TMPDIR"

# Test: calibration generator produces 50 cases
echo "Test: calibration 50 cases"
python3 "$ROOT/calibration/generate_cases.py" >/dev/null
n_cases=$(python3 -c "import json; print(json.load(open('$ROOT/calibration/cases.json'))['cases'])")
if [ "$n_cases" = "50" ]; then
  echo "  PASS: calibration cases.json has 50"
else
  echo "  FAIL: expected 50 cases, got $n_cases"
  rc=1
fi

echo ""
if [ "$rc" -eq 0 ]; then
  echo "ALL TESTS PASS ✅"
else
  echo "SOME TESTS FAIL ❌"
fi
exit $rc
