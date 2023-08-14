.PHONY: install test run

install:
	poetry install

test:
	poetry run pytest

run:
	poetry run python manage.py


