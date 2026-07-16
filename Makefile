.PHONY: help dogfood preflight health install test clean \
	bench cal ship-check conductor-help version

VERSION := $(shell cat VERSION 2>/dev/null || echo 5.1.0)

help:
	@echo "Adaptoid OS v$(VERSION) — Make targets"
	@echo ""
	@echo "  make ship-check   — full product gate (use this)"
	@echo "  make dogfood      — kit self-validation"
	@echo "  make test         — full test suite"
	@echo "  make bench        — Core speed/correctness"
	@echo "  make cal          — calibration smoke"
	@echo "  make preflight    — validators on this repo"
	@echo "  make health       — health check"
	@echo "  make install      — install script"
	@echo "  make clean        — temp files"
	@echo ""
	@echo "Generate a project (direct):"
	@echo "  python3 adaptor/engine.py --brief 'YOUR IDEA' --output ../proj --core-only --host all"

dogfood:
	bash validators/dogfood.sh

preflight:
	bash validators/preflight.sh .

health:
	bash scripts/healthcheck.sh .

install:
	bash install.sh

test:
	bash tests/run_tests.sh

bench:
	bash benchmarks/run_bench.sh

cal:
	bash calibration/run_calibration_smoke.sh

ship-check:
	bash scripts/ship_check.sh

conductor-help:
	python3 conductor/conductor.py -h

version:
	@cat VERSION

clean:
	find . -name '*.bak' -delete
	find . -name '.DS_Store' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	rm -f benchmarks/last_results.json
