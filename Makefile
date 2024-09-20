.PHONY: help copy-envs setup install requirements pre-commit safety run-local test clean

PROJECT_NAME := codeflix-catalog-admin-api

help: ## Show help
	@printf "A set of development commands.\n"
	@printf "\nUsage:\n"
	@printf "\t make \033[36m<commands>\033[0m\n"
	@printf "\nThe Commands are:\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Setup poetry environment - Create virtualenv and activate it
	poetry shell

install: ## Install poetry packages
	poetry install --sync
	poetry run pre-commit install

install-new-dependencies: ## Install new dependencies
	poetry lock --no-update
	poetry install --sync

pre-commit: ## Run the pre-commit config
	poetry run pre-commit run -a

run: ## Run server locally
	poetry run python main.py

run-docker: ## Create containers
	docker-compose up -d

test: ## Run tests locally
	poetry run pytest

clean: ## Clean up
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .coverage
	rm -rf  coverage_html
	rm -rf .pytest_cache
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf celerybeat-schedule
	rm -rf *.pyc
	rm -rf *__pycache__
	rm -rf .mypy_cache
