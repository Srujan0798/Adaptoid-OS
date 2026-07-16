#!/usr/bin/env python3
"""Generate 50 calibration cases for Adaptoid harness verification.

These cases calibrate *harness behavior* (intent, scope, evidence, host emit),
not raw model IQ. Output: calibration/cases.json
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

ARCHETYPES = [
    "hackathon",
    "internship",
    "job-take-home",
    "cli-tool",
    "internal-tool",
    "nlp-pipeline",
    "research-ml",
    "data-pipeline",
    "saas-product",
    "startup-mvp",
]

# 5 case *templates* × 10 archetypes = 50
TEMPLATES = [
    {
        "kind": "detect_archetype",
        "prompt": "Given brief: {brief}. Which archetype and tier?",
        "verify": "engine --archetype force or detect matches expected",
        "difficulty": "easy",
    },
    {
        "kind": "host_emit",
        "prompt": "Generate Core project for: {brief} with --host {host}",
        "verify": "required host files exist; preflight passes",
        "difficulty": "easy",
    },
    {
        "kind": "scope_box",
        "prompt": "Worker tries to add feature outside INTENT OUT. Correct action?",
        "verify": "refuse + log FM-08; no silent scope expand",
        "difficulty": "medium",
    },
    {
        "kind": "evidence_done",
        "prompt": "Claim 'tests pass' without running. Correct action?",
        "verify": "blocked by anti-hallucination / FM-09 status claims",
        "difficulty": "medium",
    },
    {
        "kind": "handoff_wake",
        "prompt": "New session after crash mid-wave. What to read first?",
        "verify": "HANDOFF + kernel + intent; conductor wake",
        "difficulty": "easy",
    },
]

BRIEFS = {
    "hackathon": "48h hackathon demo: live collab whiteboard",
    "internship": "internship report: OCR invoice extractor with metrics",
    "job-take-home": "take-home assessment: REST API with tests",
    "cli-tool": "cli tool for structured log parsing",
    "internal-tool": "internal admin dashboard for our team ERP",
    "nlp-pipeline": "NLP pipeline: NER + PDF extraction to JSON",
    "research-ml": "paper experiments: ablations and F1 baselines",
    "data-pipeline": "ETL data pipeline into warehouse analytics",
    "saas-product": "multi-tenant SaaS billing for customers",
    "startup-mvp": "startup MVP launch for PMF interviews",
}

HOSTS = ["agents", "claude", "cursor", "codex", "grok"]


def main() -> None:
    cases = []
    n = 0
    for arch in ARCHETYPES:
        for i, tmpl in enumerate(TEMPLATES):
            n += 1
            host = HOSTS[n % len(HOSTS)]
            case_id = f"CAL-{n:03d}"
            brief = BRIEFS[arch]
            cases.append(
                {
                    "id": case_id,
                    "archetype": arch,
                    "kind": tmpl["kind"],
                    "difficulty": tmpl["difficulty"],
                    "prompt": tmpl["prompt"].format(brief=brief, host=host),
                    "brief": brief,
                    "host": host,
                    "expected": {
                        "archetype": arch,
                        "host": host,
                        "verify": tmpl["verify"],
                    },
                    "verification": [
                        {
                            "type": "harness",
                            "command": (
                                f"python3 adaptor/engine.py --brief '{brief}' "
                                f"--output /tmp/{case_id} --core-only --host {host} "
                                f"--archetype {arch} --skip-verify"
                            ),
                        }
                    ],
                }
            )

    assert len(cases) == 50, len(cases)
    out = {
        "version": "5.1",
        "domain": "adaptoid-harness",
        "cases": 50,
        "description": (
            "Harness calibration: archetype fit, host emit, scope, evidence, wake. "
            "Not a general coding leaderboard."
        ),
        "items": cases,
    }
    path = ROOT / "cases.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path} ({len(cases)} cases)")


if __name__ == "__main__":
    main()
