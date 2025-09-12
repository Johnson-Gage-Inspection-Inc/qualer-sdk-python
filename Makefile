.PHONY: help install install-dev test test-cov lint format type-check build clean docs

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package in editable mode
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .

test:  ## Run tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage
	pytest tests/ -v --cov=qualer_sdk --cov-report=html --cov-report=term-missing

lint:  ## Run linting checks
	flake8 src/qualer_sdk --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/qualer_sdk --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:  ## Format code with black and isort
	black src/qualer_sdk tests/
	isort src/qualer_sdk tests/

type-check:  ## Run type checking with mypy
	mypy src/qualer_sdk

build:  ## Build package
	python -m build

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete



check-all: lint type-check test  ## Run all checks (lint, type-check, test)

ci: install-dev check-all build  ## Run full CI pipeline locally
