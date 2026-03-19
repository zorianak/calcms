SHELL := /bin/bash

postgres:
	@echo "Starting Postgres"
	ls
	docker compose -f apps/api/docker-compose.yml up -d postgres
	@echo "Checking for Postgres to be healthy.."
	@until docker compose -f apps/api/docker-compose.yml ps postgres | grep -q "healthy"; do \
		echo "Still waiting (:"; \
		sleep 2; \
	done
	@echo "Postgres ate its carrots (:"
	docker compose -f apps/api/docker-compose.yml ps
api:
	@echo "Starting API"
	cd apps/api && uv sync
	cd apps/api && uv run calcms-preflight
	cd apps/api && uv run python -m calcms_api.main
start: postgres api
alembic:
	cd apps/api && uv run alembic upgrade head
stop: 
	docker compose -f apps/api/docker-compose.yml down
