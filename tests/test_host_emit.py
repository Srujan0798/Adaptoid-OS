#!/usr/bin/env python3
"""Integration tests for Core kit + host adapters."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / "adaptor" / "engine.py"
sys.path.insert(0, str(ROOT / "adaptor"))
from host_emit import parse_hosts, emit_hosts, build_context  # noqa: E402


class TestParseHosts(unittest.TestCase):
    def test_default_when_empty(self):
        self.assertEqual(parse_hosts(""), ["agents", "claude"])
        self.assertEqual(parse_hosts(None), ["agents", "claude"])

    def test_all(self):
        h = parse_hosts("all")
        self.assertIn("claude", h)
        self.assertIn("cursor", h)
        self.assertIn("grok", h)
        self.assertEqual(len(h), 5)

    def test_csv(self):
        self.assertEqual(parse_hosts("cursor,codex"), ["cursor", "codex"])

    def test_unknown(self):
        with self.assertRaises(ValueError):
            parse_hosts("vscode")


class TestEmitHosts(unittest.TestCase):
    def test_claude_and_agents(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            ctx = build_context(
                project_name="demo",
                goal="ship a demo",
                archetype="cli-tool",
                tier="T0",
                host="agents,claude",
            )
            written = emit_hosts(tmp, ["agents", "claude"], ctx)
            self.assertIn("AGENTS.md", written)
            self.assertIn("CLAUDE.md", written)
            self.assertTrue((tmp / "AGENTS.md").exists())
            self.assertTrue((tmp / "CLAUDE.md").exists())
            self.assertTrue((tmp / ".claude" / "hooks" / "session-start.sh").exists())
            self.assertTrue((tmp / ".claude" / "hooks" / "pre-tool-use.sh").exists())
            settings = tmp / ".claude" / "settings.json"
            self.assertTrue(settings.exists())
            self.assertIn("PreToolUse", settings.read_text())
            body = (tmp / "AGENTS.md").read_text()
            self.assertTrue(
                "Session start" in body or "Session Start Protocol" in body or "SHIP SYSTEM" in body,
                msg="cold-start missing session orient",
            )
            self.assertIn("ship a demo", body)
        finally:
            shutil.rmtree(tmp)

    def test_cursor(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            ctx = build_context(
                project_name="demo",
                goal="cursor project",
                archetype="hackathon",
                tier="T0",
                host="cursor",
            )
            written = emit_hosts(tmp, ["cursor"], ctx)
            self.assertIn(".cursor/rules/adaptoid.mdc", written)
            self.assertTrue((tmp / "AGENTS.md").exists())
            mdc = (tmp / ".cursor" / "rules" / "adaptoid.mdc").read_text()
            self.assertIn("alwaysApply", mdc)
            self.assertIn("cursor project", mdc)
        finally:
            shutil.rmtree(tmp)


class TestEngineIntegration(unittest.TestCase):
    def _run_engine(self, *extra: str) -> tuple[int, dict, Path]:
        tmp = Path(tempfile.mkdtemp())
        out = tmp / "proj"
        cmd = [
            sys.executable,
            str(ENGINE),
            "--brief",
            "test cli tool for log parsing",
            "--output",
            str(out),
            "--skip-verify",
            *extra,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        payload = {}
        if proc.returncode == 0:
            # stdout is JSON
            try:
                payload = json.loads(proc.stdout)
            except json.JSONDecodeError:
                payload = {"raw": proc.stdout, "stderr": proc.stderr}
        else:
            payload = {"stderr": proc.stderr, "stdout": proc.stdout}
        return proc.returncode, payload, out

    def test_core_only_all_hosts(self):
        rc, payload, out = self._run_engine("--core-only", "--host", "all")
        self.assertEqual(rc, 0, msg=str(payload))
        self.assertEqual(payload.get("kit"), "core")
        self.assertTrue((out / "kernel" / "PRINCIPLES.md").exists())
        self.assertTrue((out / "AGENTS.md").exists())
        self.assertTrue((out / "CLAUDE.md").exists())
        self.assertTrue((out / ".cursor" / "rules" / "adaptoid.mdc").exists())
        self.assertTrue((out / "HANDOFF.md").exists())
        self.assertTrue((out / "PROJECT-INTENT.md").exists())
        self.assertTrue((out / "orchestrator" / "scripts" / "preflight.sh").exists())
        self.assertTrue((out / ".adaptoid-kit").exists())
        self.assertEqual((out / ".adaptoid-kit").read_text().strip(), "core")
        # Core should not copy full pro dogfood-only validators if missing from list
        # but must have check_handoff
        self.assertTrue((out / "orchestrator" / "scripts" / "check_handoff.sh").exists())
        shutil.rmtree(out.parent)

    def test_claude_only_still_has_agents(self):
        rc, payload, out = self._run_engine("--core-only", "--host", "claude")
        self.assertEqual(rc, 0, msg=str(payload))
        self.assertTrue((out / "CLAUDE.md").exists())
        self.assertTrue((out / "AGENTS.md").exists(), "AGENTS.md guaranteed for Core")
        shutil.rmtree(out.parent)

    def test_force_archetype(self):
        rc, payload, out = self._run_engine(
            "--core-only",
            "--host",
            "agents",
            "--archetype",
            "hackathon",
            "--tier",
            "T0",
        )
        self.assertEqual(rc, 0, msg=str(payload))
        self.assertEqual(payload.get("archetype"), "hackathon")
        self.assertEqual(payload.get("tier"), "T0")
        shutil.rmtree(out.parent)


if __name__ == "__main__":
    unittest.main()
