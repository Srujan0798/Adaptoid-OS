#!/usr/bin/env bash
# Adaptoid Core — Claude Code PreToolUse hook (hard enforcement, FM-18 blast radius).
# Reads the tool call JSON on stdin. Exit 2 = block (stderr goes back to the agent).
# Scope: only hard-blocks commands with near-zero legitimate use inside a project.
set -uo pipefail

INPUT=$(cat)

TOOL=$(printf '%s' "$INPUT" | python3 -c "import sys,json;print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null || echo "")
[ "$TOOL" = "Bash" ] || exit 0

CMD=$(printf '%s' "$INPUT" | python3 -c "import sys,json;print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null || echo "")
[ -n "$CMD" ] || exit 0

deny() {
  echo "[adaptoid] BLOCKED (FM-18 blast radius): $1 — pause and confirm with the human (kernel law 6)." >&2
  exit 2
}

case "$CMD" in
  *'rm -rf /'*|*'rm -rf ~'*|*'rm -rf "$HOME"'*|*'rm -rf $HOME'*) deny "recursive delete outside the project" ;;
esac

printf '%s' "$CMD" | grep -qE 'git push[^|;&]*(--force|-f)([^-]|$)[^|;&]*\b(main|master)\b' && deny "force-push to protected branch"
printf '%s' "$CMD" | grep -qE 'curl[^|;&]*\|[[:space:]]*(sudo[[:space:]]+)?(ba|z)?sh\b' && deny "piping remote script to shell"

exit 0
