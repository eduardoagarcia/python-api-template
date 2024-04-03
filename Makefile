.PHONY: init build destroy start stop shell-api all

API := graphql-api

init:
	@cd api && cp -n .env.example .env || true
	docker-compose build --no-cache
	docker-compose up -d api

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

logs:
	docker logs $(API)

all: init
