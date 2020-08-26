# note: --env-file requires docker-compose>=1.25
#       ref: https://github.com/docker/compose/pull/6535

include $(ENVFILE)
export

compose_cmd = docker-compose -p alerta -f docker/docker-compose.yml --env-file .env


build:
	$(compose_cmd) build

deploy: build
	$(compose_cmd) up

stop:
	$(compose_cmd) stop

install:
	pip install -e .['develop']

test_crawlclima:
	# Ignore tests in database, waiting to resolve db_demo issue#
	pytest -v crawlclima --ignore=crawlclima/tests/test_tasks.py

test_downloader_app:
	pytest downloader_app/ -v

configure_downloader_app:
	python downloader_app/config.py

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
