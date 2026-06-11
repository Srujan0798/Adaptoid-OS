.PHONY: help dogfood preflight health install test clean

help:
	@echo "Adaptoid OS v4.0 — Make targets"
	@echo ""
	@echo "  make dogfood    — run OS self-validation"
	@echo "  make preflight  — run all wired validators"
	@echo "  make health     — run health check"
	@echo "  make install    — one-command setup"
	@echo "  make test       — run validator tests"
	@echo "  make clean      — remove temp files"

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

clean:
	find . -name '*.bak' -delete
	find . -name '.DS_Store' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
