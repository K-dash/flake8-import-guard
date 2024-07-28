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

.PHONY: output_coverage
output_coverage:
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

.PHONY: all
all: format lint test
