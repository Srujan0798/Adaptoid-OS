#!/usr/bin/env bash
# Smoke a sample of harness calibration cases through the engine.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 calibration/generate_cases.py

python3 - <<'PY'
import json, subprocess, sys, tempfile
from pathlib import Path

root = Path(".").resolve()
data = json.loads((root / "calibration/cases.json").read_text())
items = data["items"]
# sample: first case per kind (5) + last 5 = up to 10
kinds = {}
sample = []
for it in items:
    if it["kind"] not in kinds:
        kinds[it["kind"]] = it
        sample.append(it)
sample += items[-5:]
# unique by id
seen, uniq = set(), []
for it in sample:
    if it["id"] not in seen:
        seen.add(it["id"])
        uniq.append(it)

fail = 0
for it in uniq:
    brief = it["brief"]
    arch = it["archetype"]
    host = it["host"]
    out = Path(tempfile.mkdtemp()) / it["id"]
    cmd = [
        sys.executable,
        str(root / "adaptor/engine.py"),
        "--brief", brief,
        "--output", str(out),
        "--core-only",
        "--host", host,
        "--archetype", arch,
        "--skip-verify",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL {it['id']} engine rc={r.returncode}")
        print(r.stderr[-500:])
        fail += 1
        continue
    need = ["AGENTS.md", "HANDOFF.md", "kernel/PRINCIPLES.md", "PROJECT-INTENT.md"]
    if host == "claude":
        need.append("CLAUDE.md")
    if host == "cursor":
        need.append(".cursor/rules/adaptoid.mdc")
    missing = [f for f in need if not (out / f).exists()]
    if missing:
        print(f"FAIL {it['id']} missing {missing}")
        fail += 1
    else:
        print(f"OK   {it['id']} {arch} host={host}")

print(f"\ncalibration smoke: {len(uniq) - fail}/{len(uniq)} passed")
sys.exit(1 if fail else 0)
PY
