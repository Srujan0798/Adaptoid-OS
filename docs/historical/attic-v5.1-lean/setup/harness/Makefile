.PHONY: up down logs status health

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

status:
	docker-compose ps

health:
	@echo "Checking services..."
	@curl -sf http://localhost:4000/health || echo "LiteLLM not healthy"
	@curl -sf http://localhost:6333/healthz || echo "Qdrant not healthy"
	@redis-cli ping || echo "Redis not healthy"
