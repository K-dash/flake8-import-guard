.DEFAULT_GOAL := all
sources = src tests

.PHONY: install
install:
	poetry install
	poetry shell
	pre-commit install

.PHONY: format
format:
	poetry run ruff check --fix $(sources)
	poetry run ruff format $(sources)

.PHONY: lint
lint:
	poetry run ruff check $(sources)
	poetry run ruff format --check $(sources)

.PHONY: test
test:
	poetry run pytest

.PHONY: output_cov
output_cov:
	@rm -rf htmlcov
	@mkdir -p htmlcov
	poetry run coverage run -m pytest
	poetry run coverage report
	poetry run coverage html -d htmlcov

.PHONY: clean
clean:
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -f .coverage
	rm -f .coverage.*

.PHONY: build
build:
	poetry build
	python -m venv test_env
	source test_env/bin/activate

.PHONY: build_test
build_test:
	pip install dist/flake8_import_guard-0.1.1-py3-none-any.whl
	flake8 --version

.PHONY: all
all: format lint test
