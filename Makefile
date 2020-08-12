up:
	docker-compose -f docker-compose-dev.yml up -d $(filter-out $@,$(MAKECMDGOALS))

build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f docker-compose-dev.yml build $(filter-out $@,$(MAKECMDGOALS))

stop:
	docker-compose -f docker-compose-dev.yml stop $(filter-out $@,$(MAKECMDGOALS))


run:
	docker-compose -f docker-compose-dev.yml run --rm  $(filter-out $@,$(MAKECMDGOALS))


bash:
	 docker exec -it django-biolerplate-backend /bin/bash

logs:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml logs -f --tail=70 $(filter-out $@,$(MAKECMDGOALS))

down:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml down


install-pre-commit: install-test-requirements
	pre-commit install --install-hooks