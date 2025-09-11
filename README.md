# qualer-sdk-python

[![Last Commit](https://img.shields.io/github/last-commit/Johnson-Gage-Inspection-Inc/qualer-sdk-python)](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/commits/main)
[![CI](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/workflows/CI/badge.svg)](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/actions)
[![codecov](https://codecov.io/gh/Johnson-Gage-Inspection-Inc/qualer-sdk-python/branch/main/graph/badge.svg)](https://codecov.io/gh/Johnson-Gage-Inspection-Inc/qualer-sdk-python)
[![Python Versions](https://img.shields.io/badge/python-3.9+-blue)](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python)
[![Qualer API](https://img.shields.io/badge/Qualer%20API-v1-orange)](https://jgiquality.qualer.com/swagger/ui/index)

This repository contains the Python client for the Qualer API. It provides client classes and models for interacting with the Qualer API.

## Features

- **Well-typed Client:** Maintained code with strong typing and tests.
- **Modern Python Support:** Compatible with Python 3.8+.
- **Extensive API Coverage:** See the [API Documentation](docs/) for details on available endpoints and models.
- **Type Hints:** Full typing support for better IDE integration.
- **Comprehensive Testing:** Automated testing with pytest and coverage reporting.

## Installation

You can install the package using either `pip` or `setuptools`.

### Using pip

```sh
pip install git+https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python.git
```

### Using setuptools

```sh
python setup.py install --user
```

## Usage

After installing, import and use the package in your Python code:

```python
import os
from qualer_sdk import AuthenticatedClient
from qualer_sdk.api.report_datasets import get_service_orders

# Initialize the client with authentication token from environment variable
# (base_url defaults to https://api.johnson-gage.com)
client = AuthenticatedClient(token=os.getenv("QUALER_API_TOKEN"))

# Call API endpoints directly
service_orders = get_service_orders.sync(client=client, customer_id=12345)
print(service_orders)

# Or use async
import asyncio
async def main():
    service_orders = await get_service_orders.asyncio(client=client, customer_id=12345)
    print(service_orders)

asyncio.run(main())
```

For more details on each API, refer to the generated [API documentation](docs/).

## Authentication

The SDK supports token-authenticated requests using the `AuthenticatedClient` class. The base URL defaults to the correct Qualer API endpoint:

```python
import os
from qualer_sdk import AuthenticatedClient
from qualer_sdk.api.report_datasets import get_as_found_measurements_by_order

# Initialize with token from environment variable (recommended)
# (base_url defaults to https://api.johnson-gage.com)
client = AuthenticatedClient(token=os.getenv("QUALER_API_TOKEN"))

# Call authenticated endpoints
measurements = get_as_found_measurements_by_order.sync(
    client=client, 
    service_order_id=285227
)
print(measurements)
```

**Setting up your API token:**

Set the environment variable in your shell:
```bash
# Linux/macOS
export QUALER_API_TOKEN="your-actual-token-here"

# Windows Command Prompt
set QUALER_API_TOKEN=your-actual-token-here

# Windows PowerShell
$env:QUALER_API_TOKEN="your-actual-token-here"
```

Or create a `.env` file in your project root:
```
QUALER_API_TOKEN=your-actual-token-here
```

Then load it in your Python code using `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
```

You can also override the base URL if needed:

```python
client = AuthenticatedClient(
    base_url="https://custom-api-endpoint.com",
    token="your-api-token-here"
)
```


## Development

### Setting up Development Environment

1. Clone the repository:
```sh
git clone https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python.git
cd qualer-sdk-python
```

2. Install development dependencies:
```sh
pip install -r requirements-dev.txt
pip install -e .
```

3. (Optional) Set up pre-commit hooks:
```sh
pre-commit install
```

### Development Commands

The project includes a Makefile with convenient commands:

```sh
make help           # Show available commands
make install        # Install package in editable mode
make install-dev    # Install development dependencies
make test           # Run tests
make test-cov       # Run tests with coverage
make lint           # Run linting checks
make format         # Format code with black and isort
make type-check     # Run type checking with mypy
make build          # Build package
make clean          # Clean build artifacts
make regenerate     # Regenerate SDK from OpenAPI spec
make check-all      # Run all checks (lint, type-check, test)
make ci             # Run full CI pipeline locally
```

### Running Tests

Run the test suite:
```sh
pytest tests/ -v
```

Run tests with coverage:
```sh
pytest tests/ -v --cov=qualer_sdk --cov-report=html
```

### Code Quality

The project uses several tools for code quality:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking
- **pytest** for testing with coverage

## CI/CD

This project uses GitHub Actions for continuous integration:

- **Testing:** Automated testing across Python 3.8-3.12
- **Linting:** Code quality checks with flake8
- **Type Checking:** Static analysis with mypy
- **Coverage:** Test coverage reporting with codecov
- **Building:** Package building and validation
- **Publishing:** Automatic PyPI publishing on tagged releases (optional)

### GitHub Actions Workflows

- **CI Pipeline** (`.github/workflows/ci.yml`): Runs on every push and PR
- **Dependabot** (`.github/dependabot.yml`): Automated dependency updates

## Prerequisites

### Note on generation

Historically some files were generated from an OpenAPI spec. We no longer maintain a regeneration pipeline; modify code directly in `src/qualer_sdk/**` as needed.

## Contributing guidelines

It's okay to modify code anywhere in the repo, including generated code under `src/qualer_sdk/*`. We are no longer maintaining a regeneration pipeline.

## Running Tests

The repository includes comprehensive tests for various API endpoints and functionality. You can run the tests using `pytest`:

```sh
# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=qualer_sdk --cov-report=html

# Run a focused test file
pytest tests/test_assets_api.py -v
```

## Repository Structure

```
qualer-sdk-python/
├── .github/                    # GitHub Actions workflows and config
│   ├── workflows/
│   │   └── ci.yml             # CI/CD pipeline
│   └── dependabot.yml         # Dependency update config
├── src/
│   └── qualer_sdk/            # Main package source code
│       ├── __init__.py        # Package initialization
│       ├── api/               # API endpoint classes
│       └── models/            # Data model classes
├── tests/                     # Unit tests
├── docs/                      # Generated API documentation
├── templates/                 # Legacy template files (not used by pipeline)
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── Makefile                   # Development commands
├── pyproject.toml             # Modern Python packaging config
├── requirements.txt           # Runtime dependencies
├── requirements-dev.txt       # Development dependencies
├── setup.py                   # Legacy packaging script
```

### Key Changes from Original Structure

The repository has been restructured to follow modern Python packaging standards:
- Moved from nested `src/qualer_sdk/qualer_sdk/` to clean `src/qualer_sdk/`
- Tests moved from `src/qualer_sdk/test/` to standard `tests/` directory
- Documentation moved from `src/qualer_sdk/docs/` to standard `docs/` directory
- Added modern `pyproject.toml` with comprehensive build configuration
- Enhanced CI/CD pipeline with GitHub Actions
- **Refactored SDK generation**: Template files moved from embedded strings to modular files in `templates/` directory for better maintainability

## Contributing

Contributions to improve the SDK or scripts are welcome. Please fork this repository and submit a pull request with your changes.

## License

This project is provided “as-is” without any warranty. See the LICENSE file for more information.
