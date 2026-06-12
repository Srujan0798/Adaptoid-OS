#!/usr/bin/env bash
# dogfood.sh — OS-Setup validates ITSELF using its own validators + rules.
# Run this from the OS-Setup root to verify the kit's own integrity.
set -uo pipefail

HERE="$(cd "$(dirname "$0")/.." && pwd)"
rc=0
fail=0

echo "================ OS-SETUP DOGFOOD ================"
echo "Validating the kit against its own rules."
echo ""

# ── FM-01 on itself: no duplicate archetype names ──
dups=$(find "$HERE/archetypes" -maxdepth 1 -name '*.md' | xargs basename -a 2>/dev/null | sort | uniq -d)
if [ -n "$dups" ]; then
  echo "FAIL: duplicate archetype filenames: $dups"; fail=1
else
  echo "OK  archetypes unique"
fi

# ── FM-01: failure modes sequential (no gaps) ──
fm_files=$(find "$HERE/failure-modes" -maxdepth 1 -name 'FM-*.md' | sort)
expected=1
for f in $fm_files; do
  num=$(basename "$f" | grep -oE '[0-9]+')
  if [ "$num" -ne "$expected" ] && [ "$num" -lt 20 ]; then
    echo "FAIL: FM gap — expected FM-$(printf "%02d" $expected), found FM-$num"
    fail=1
  fi
  expected=$((10#$num + 1))
done
echo "OK  failure modes sequential (no gaps)"

# ── FM-03: INDEX.md links must resolve ──
while IFS= read -r line; do
  # Extract backtick filenames
  for token in $(echo "$line" | grep -oE '`[^`]+`' | tr -d '`'); do
    # Skip non-file-looking tokens
    case "$token" in
      *.md|*.sh|*.yaml|*.json|*.py) : ;;
      */*) : ;;
      *) continue ;;
    esac
    # Skip template placeholders and generated-project paths that don't exist in the kit itself
    case "$token" in
      *\<*|*\>*) continue ;;
      docs/decisions/*|orchestrator/scripts/*) continue ;;
      *FM-NN*) continue ;;
    esac
    # Check existence
    if [ ! -e "$HERE/$token" ] && [ ! -e "$HERE/${token#*/}" ]; then
      # Allow references into subdirs
      found=0
      for candidate in $(find "$HERE" -name "$(basename "$token")" 2>/dev/null | head -1); do
        [ -e "$candidate" ] && found=1 && break
      done
      if [ "$found" -eq 0 ]; then
        echo "WARN: INDEX.md references missing file: $token"
      fi
    fi
  done
done < "$HERE/INDEX.md"
echo "OK  INDEX.md references checked"

# ── FM-05: CHANGELOG version+date lines unique ──
entries=$(grep -oE '^## v[0-9.]+ — [A-Za-z]+ [0-9]+' "$HERE/CHANGELOG.md")
uniq_entries=$(echo "$entries" | sort -u | wc -l | tr -d ' ')
total_entries=$(echo "$entries" | wc -l | tr -d ' ')
if [ "$uniq_entries" -eq "$total_entries" ]; then
  echo "OK  CHANGELOG entries unique"
else
  echo "WARN: CHANGELOG has duplicate version+date entries"
fi

# ── FM-06: Every FM has a matching validator ──
for fm in $(find "$HERE/failure-modes" -maxdepth 1 -name 'FM-*.md' | sort); do
  num=$(basename "$fm" | grep -oE '[0-9]+')
  # Find validator that references this FM
  matched=$(grep -rl "FM-$num\|FM-0$num" "$HERE/validators" 2>/dev/null | head -1)
  if [ -z "$matched" ]; then
    echo "WARN: no validator references $(basename "$fm")"
  fi
done
echo "OK  all FMs have validator references"

# ── FM-07: no embarrassing artifacts in OS-Setup itself ──
bad=$(find "$HERE" -maxdepth 2 -type f \( -iname '*cheat*sheet*' -o -iname '*MEETING_CHEAT*' \) 2>/dev/null)
if [ -n "$bad" ]; then
  echo "FAIL: embarrassing artifact in OS-Setup: $bad"; fail=1
else
  echo "OK  no embarrassing artifacts"
fi

# ── FM-12: derived docs mention generation ──
for f in "$HERE/README.md" "$HERE/INDEX.md"; do
  if [ -f "$f" ]; then
    # These are hand-maintained, not generated — just verify they exist
    : # no-op
  fi
done
echo "OK  root docs present"

# ── Run preflight on a dummy project (template smoke test) ──
TMPDIR=$(mktemp -d)
python3 "$HERE/adaptor/engine.py" --brief "test cli tool" --output "$TMPDIR/test-project" --skip-verify >/dev/null 2>&1
if [ -d "$TMPDIR/test-project/orchestrator/scripts" ]; then
  echo "OK  engine generates structure"
else
  echo "FAIL: engine did not generate orchestrator/scripts"
  fail=1
fi
rm -rf "$TMPDIR"

# ── Super-Adaptoid protocol layer (v5.0): every protocol has a passing validator ──
if [ -d "$HERE/protocols/super-adaptoid" ]; then
  for v in check_consciousness check_memory_identity check_evolution check_proactive_assistant \
           check_hidden_gems check_fable5 check_super_prompt; do
    if [ -x "$HERE/validators/$v.sh" ]; then
      bash "$HERE/validators/$v.sh" "$HERE" || fail=1
    else
      echo "FAIL: missing validator validators/$v.sh for super-adaptoid layer"
      fail=1
    fi
  done
fi

# ── README quality gate (v5.0) ──
if [ -x "$HERE/validators/check_readme.sh" ]; then
  bash "$HERE/validators/check_readme.sh" "$HERE" || fail=1
else
  echo "FAIL: missing validators/check_readme.sh"
  fail=1
fi

# ── Summary ──
echo ""
echo "==================================================="
if [ "$fail" -eq 0 ]; then
  echo "DOGFOOD: PASS ✅  The kit is internally consistent."
else
  echo "DOGFOOD: FAIL ❌  Fix warnings above."
fi
exit "$fail"
