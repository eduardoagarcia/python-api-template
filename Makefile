.PHONY: init build destroy start stop shell-api all

API := template-api

init:
	@cd api && cp -n .env.example .env || true
	docker-compose build --no-cache
	docker-compose up -d postgres
	@echo "Waiting 10 seconds for postgres to boot..."
	@sleep 10
	docker-compose up -d api
	docker exec -it $(API) sh -c "alembic upgrade head"

build:
	docker-compose build --no-cache

destroy:
	docker-compose down

start:
	docker-compose up -d

stop:
	docker-compose stop

shell:
	docker exec -it $(API) sh

poetry-install:
	cd api && poetry install

run-tests:
	cd api && poetry run pytest

run-migrations:
	docker exec -it $(API) sh -c "alembic upgrade head"

logs:
	docker logs $(API)

all: init
