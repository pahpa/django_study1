check_defined = \
$(strip $(foreach 1,$1, \
$(call __check_defined,$1,$(strip $(value 2)))))

__check_defined = \
$(if $(value $1),, \
$(error Undefined $1$(if $2, ($2))))

.PHONY: list
list:
	@awk -F: '!/(check|^if*|^else|^endif)/ && /^[A-z]/ {print $$1}' Makefile

clean:
	python manage.py clean_pyc

compile:
	python manage.py compile_pyc

celeryd-run:
	@celery -A django_study worker -c 2 -D --pidfile=/var/tmp/wiki_c.pid --logfile=/var/tmp/wiki_c.log -E --beat --scheduler django --loglevel=info

celery-kill:
	@kill `cat /var/tmp/wiki_c.pid`

celery-run:
	@celery -A django_study worker -c 2 -E --beat --scheduler django --loglevel=info

runserver-dev:
	@python manage.py runserver

runserver:
	@gunicorn --reload django_study.asgi:application -k uvicorn.workers.UvicornWorker 

createdatacelerytests:
	@python manage.py create_celery_config --force

createdatatests:
	@python manage.py create_fake_data --force

requirements:
	pip install -r requirements.txt

requirements-tests:
	pip install -r requirements-tests.txt

migrate:
	python manage.py migrate

docker:
	docker kill django-study || true
	docker rm -f django-study || true
	docker image rm -f django-study:0.0.0 || true
	docker build . -t django-study:0.0.0
	docker run --name django-study -p 127.0.0.1:8000:8000 django-study:0.0.0