.PHONY: env run docs docs-init test lint
.DEFAULT: env

SHELL := /bin/bash

# List and check for commands.
COMMANDS = make 
COMMAND_CHECK := $(foreach exec,$(COMMANDS), $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

env:
	@echo "Building the flask environment..."
	@poetry install

run:
	@source .env; poetry run flask run

lint:
	@poetry run isort --virtual-env .venv **/*.py && poetry run flake8

docs:
	@cd docs && make html

docs-init:
	@poetry run sphinx-apidoc -o docs/source ./ ./tests/*.py
	@cd docs && make html

test:
