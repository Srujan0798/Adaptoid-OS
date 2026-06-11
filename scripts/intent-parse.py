#!/usr/bin/env python3
"""Parse PROJECT-INTENT.md YAML frontmatter against JSON Schema."""
import sys, json, yaml, argparse
from pathlib import Path

def parse_intent(path: Path, schema_path: Path):
    text = path.read_text()
    lines = text.splitlines()
    if lines[0].strip() != '---':
        print("FAIL: missing YAML frontmatter")
        sys.exit(1)
    end = lines.index('---', 1)
    front = yaml.safe_load('\n'.join(lines[1:end]))
    schema = json.loads(schema_path.read_text())
    try:
        import jsonschema
        jsonschema.validate(front, schema)
        print("OK: PROJECT-INTENT.md valid")
        print(json.dumps(front, indent=2))
    except ImportError:
        print("WARN: jsonschema not installed; skipping validation")
        print(json.dumps(front, indent=2))
    except jsonschema.ValidationError as e:
        print(f"FAIL: {e.message}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("intent", type=Path)
    parser.add_argument("--schema", type=Path, default=Path("schemas/ProjectIntent.schema.json"))
    args = parser.parse_args()
    parse_intent(args.intent, args.schema)
