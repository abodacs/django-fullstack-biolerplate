up:
	docker-compose -f docker-compose-dev.yml up -d $(filter-out $@,$(MAKECMDGOALS))

build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f docker-compose-dev.yml build $(filter-out $@,$(MAKECMDGOALS))

stop:
	docker-compose -f docker-compose-dev.yml stop $(filter-out $@,$(MAKECMDGOALS))

activate:
	source $HOME/online_benevolent/bin/activate

run:
	docker-compose -f docker-compose-dev.yml run --rm  $(filter-out $@,$(MAKECMDGOALS))

bash:
	docker-compose  -f docker-compose-dev.yml run --rm backend bash

makemigrations:
	docker-compose -f docker-compose-dev.yml  run --rm backend python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f docker-compose-dev.yml  run --rm backend python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))


logs:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml logs -f --tail=70 $(filter-out $@,$(MAKECMDGOALS))

down:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml down


psql:
	docker-compose -f docker-compose-dev.yml run --rm postgres psql -U $POSTGRES_USER $POSTGRES_DB

install-pre-commit: install-test-requirements
	pre-commit install --install-hooks
