.PHONY: help dogfood preflight health install test clean \
	bench cal core-demo ship-check conductor-help version

VERSION := $(shell cat VERSION 2>/dev/null || echo 5.1.0)

help:
	@echo "Adaptoid OS v$(VERSION) — Make targets"
	@echo ""
	@echo "  make dogfood      — kit self-validation"
	@echo "  make preflight    — validators on this repo"
	@echo "  make health       — health check"
	@echo "  make test         — full test suite"
	@echo "  make bench        — Core speed/correctness benchmarks"
	@echo "  make cal          — generate + smoke calibration cases"
	@echo "  make core-demo    — generate demo Core project under /tmp"
	@echo "  make ship-check   — release gate (dogfood+tests+bench+cal)"
	@echo "  make install      — one-command setup"
	@echo "  make clean        — remove temp files"

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

core-demo:
	python3 adaptor/engine.py \
		--brief "48h hackathon: realtime collab whiteboard" \
		--output /tmp/adaptoid-core-demo \
		--core-only \
		--host all \
		--skip-verify
	python3 conductor/conductor.py init-wave --project /tmp/adaptoid-core-demo -n 3
	python3 conductor/conductor.py status --project /tmp/adaptoid-core-demo
	@echo "Demo at /tmp/adaptoid-core-demo"

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
