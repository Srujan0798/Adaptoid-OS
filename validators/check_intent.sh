#!/usr/bin/env bash
# Validates PROJECT-INTENT.md YAML frontmatter against JSON Schema.
# Usage: check_intent.sh [project_root] [--fix] [--dry-run]
set -uo pipefail
ROOT="${1:-.}"
INTENT="$ROOT/PROJECT-INTENT.md"
SCHEMA="$ROOT/schemas/ProjectIntent.schema.json"
[ -f "$SCHEMA" ] || SCHEMA="$ROOT/../schemas/ProjectIntent.schema.json"

if [ ! -f "$INTENT" ]; then
  echo "OK check-intent: no PROJECT-INTENT.md found (optional for small projects)"
  exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "WARN check-intent: python3 not available; skipping schema validation"
  exit 0
fi

python3 -c "
import json, sys
try:
    import yaml, jsonschema
except ImportError as e:
    print(f'WARN check-intent: missing dependency {e}')
    sys.exit(0)

from pathlib import Path
intent_file = Path('$INTENT')
schema_file = Path('$SCHEMA')
if not schema_file.exists():
    print('WARN check-intent: schema not found')
    sys.exit(0)

lines = intent_file.read_text().splitlines()
if not lines or lines[0].strip() != '---':
    print('FAIL check-intent: PROJECT-INTENT.md missing YAML frontmatter')
    sys.exit(1)
try:
    end = lines.index('---', 1)
except ValueError:
    print('FAIL check-intent: PROJECT-INTENT.md frontmatter not closed')
    sys.exit(1)
front = yaml.safe_load('\n'.join(lines[1:end]))
schema = json.loads(schema_file.read_text())
try:
    jsonschema.validate(front, schema)
    print('OK check-intent: PROJECT-INTENT.md valid')
except jsonschema.ValidationError as e:
    print(f'FAIL check-intent: schema validation error: {e.message}')
    sys.exit(1)
except Exception as e:
    print(f'FAIL check-intent: {e}')
    sys.exit(1)
" || exit 1
