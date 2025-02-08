.DEFAULT_GOAL := all
sources = src tests

.PHONY: install
install:
	uv install
	uv shell
	pre-commit install

.PHONY: format
format:
	uv run ruff check --fix $(sources)
	uv run ruff format $(sources)

.PHONY: lint
lint:
	uv run ruff check $(sources)
	uv run ruff format --check $(sources)

.PHONY: test
test:
	uv run pytest

.PHONY: output_cov
output_cov:
	@rm -rf htmlcov
	@mkdir -p htmlcov
	uv run coverage run -m pytest
	uv run coverage report
	uv run coverage html -d htmlcov

.PHONY: clean
clean:
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -f .coverage
	rm -f .coverage.*

.PHONY: build
build:
	uv build
	python -m venv test_env
	source test_env/bin/activate

.PHONY: build_test
build_test:
	pip install dist/flake8_import_guard-1.0.0-py3-none-any.whl
	flake8 --version

.PHONY: all
all: format lint test

# CI test
.PHONY: ci
test-ci:
	uv run pytest --cov=./src --cov-report=xml
