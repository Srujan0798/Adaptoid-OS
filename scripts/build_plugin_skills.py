#!/usr/bin/env python3
"""Materialize the engine's ADAPTOID_SKILLS into the plugin `skills/` dir.

Single truth stays in adaptor/engine.py — this script reuses
emit_adaptoid_skills() so plugin skills can never drift from emitted ones.
Run via `make plugin-skills` after editing ADAPTOID_SKILLS.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_engine():
    sys.path.insert(0, str(ROOT / "adaptor"))
    spec = importlib.util.spec_from_file_location(
        "adaptoid_engine", ROOT / "adaptor" / "engine.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    engine = load_engine()
    out = ROOT / "skills"
    with tempfile.TemporaryDirectory() as tmp:
        engine.emit_adaptoid_skills(Path(tmp))
        src = Path(tmp) / ".agents" / "skills"
        for skill_dir in sorted(p for p in src.iterdir() if p.is_dir()):
            dst = out / skill_dir.name
            dst.mkdir(parents=True, exist_ok=True)
            shutil.copy2(skill_dir / "SKILL.md", dst / "SKILL.md")
            print(f"wrote skills/{skill_dir.name}/SKILL.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
