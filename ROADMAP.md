# Adaptoid OS Roadmap

## v5.1 — Core product finish (SHIPPED)

Portable harness people can finish projects with.

- [x] **Core / Pro / Lite** ladder (`core/`, Lite OS_SETUP, full Pro kit)
- [x] Host emission: `agents`, `claude`, `cursor`, `codex`, `grok`, `all`
- [x] Engine: `--host`, `--core-only`, `--archetype`, `--tier`
- [x] Generated projects: `kernel/`, `HANDOFF.md`, intent, schema, validators
- [x] Bootstrap + install + invocation updated for Core hosts
- [x] Integration tests (`tests/test_host_emit.py`, conductor, calibration)
- [x] **Conductor** thin runtime: status / wake / init-wave / dispatch / disjoint / handoff
- [x] **Benchmarks** (`benchmarks/run_bench.sh`)
- [x] **Calibration** 50 harness cases + smoke runner
- [x] Dogfood example path (`examples/core-finish/`)
- [x] **Ship gate** (`make ship-check` / `scripts/ship_check.sh`)
- [x] Lite OS_SETUP + 00-INVOCATION refreshed for hosts/Core

## v5.0 — Public Product Layer + Super-Adaptoid (SHIPPED)
- Professional open-source README and INDEX rewrite
- docs/launch/ suite
- Super-Adaptoid protocol layer + validators

## v4.0 — Eternal Agentic Harness (SHIPPED)
- Safety core, typed intent, validators, archetypes, workflows, philosophy

## v5.2 — Optional depth (after real dogfood users)
- [ ] Deeper host hooks matrix (per-host lifecycle events)
- [ ] Claw Bridge hardening (LangGraph / CrewAI / AutoGen) when someone needs export
- [ ] Cost/accuracy model eval harness (optional; not Core)

## v5.3+ — Demand-gated only
- Multi-channel gateways, enterprise packs — **do not build until Core has users**

## Focus filter

Before new work: (1) finish a project on a host we don't control? (2) prevent a known FM with a check? (3) stranger usable in &lt;10 min? If no to all three → skip.

## Contributing
Pick any unchecked box. See CONTRIBUTING.md.
