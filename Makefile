up:
	docker-compose -f docker-compose-dev.yml up -d $(filter-out $@,$(MAKECMDGOALS))

build:
	docker-compose -f docker-compose-dev.yml build $(filter-out $@,$(MAKECMDGOALS))

stop:
	docker-compose -f docker-compose-dev.yml stop $(filter-out $@,$(MAKECMDGOALS))

activate:
	source venv/bin/activate

install-venv:
	source venv/bin/activate && python3 -m pip install -r backend/requirements.txt

run:
	docker-compose -f docker-compose-dev.yml run --rm  $(filter-out $@,$(MAKECMDGOALS))

bash:
	docker-compose  -f docker-compose-dev.yml run --rm backend bash

test:
	docker-compose  -f docker-compose-dev.yml run --rm backend python manage.py test --debug-mode $(filter-out $@,$(MAKECMDGOALS))

urls:
	docker-compose -f docker-compose-dev.yml run --rm backend python manage.py show_urls

start_celery:
	docker-compose -f docker-compose-dev.yml run --rm backend sh -c 'start_celery'

makemigrations:
	docker-compose -f docker-compose-dev.yml  run --rm backend python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f docker-compose-dev.yml  run --rm backend python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

check:
	docker-compose -f docker-compose-dev.yml  run --rm backend python3 manage.py check --deploy --settings=onlineBenevolent.settings.production

logs:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml logs -f --tail=70 $(filter-out $@,$(MAKECMDGOALS))

down:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose -f docker-compose-dev.yml down

generate_swagger:
	docker-compose -f docker-compose-dev.yml  run --rm backend python manage.py generate_swagger

psql:
	docker-compose -f docker-compose-dev.yml run --rm postgres psql -U $POSTGRES_USER $POSTGRES_DB

install-pre-commit: install-test-requirements
	pre-commit install --install-hooks
