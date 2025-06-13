# Development Workflow Guide

This document describes the complete CI/CD pipeline and development workflow for the Qualer SDK Python project.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python.git
cd qualer-sdk-python

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
pip install -e .

# Install pre-commit hooks (optional but recommended)
pre-commit install

# Run tests
pytest tests/ -v

# Run code quality checks
make lint
make type-check
make format
```

## 📁 Project Structure

```
qualer-sdk-python/
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # GitHub Actions CI/CD pipeline
│   └── dependabot.yml          # Automated dependency updates
├── src/
│   └── qualer_sdk/             # Main package source code
├── tests/                      # Test suite (422 tests)
├── docs/                       # API documentation
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── pyproject.toml              # Project configuration
├── requirements.txt            # Runtime dependencies
├── requirements-dev.txt        # Development dependencies
├── Makefile                    # Development commands
└── DEVELOPMENT.md              # This file
```

## 🔧 Development Tools

### Pre-commit Hooks

The project includes pre-commit hooks that run automatically before each commit:

- **trailing-whitespace**: Removes trailing whitespace
- **end-of-file-fixer**: Ensures files end with a newline
- **check-yaml**: Validates YAML files
- **check-added-large-files**: Prevents committing large files
- **check-merge-conflict**: Detects merge conflict markers
- **debug-statements**: Catches debug statements
- **black**: Code formatting
- **isort**: Import sorting
- **flake8**: Code linting
- **mypy**: Static type checking

### Makefile Commands

The project includes a Makefile with convenient development commands:

```bash
make help          # Show available commands
make install       # Install development dependencies
make test          # Run test suite
make test-cov      # Run tests with coverage
make lint          # Run flake8 linting
make format        # Format code with black
make format-check  # Check code formatting
make type-check    # Run mypy type checking
make build         # Build package
make clean         # Clean build artifacts
make pre-commit    # Run pre-commit on all files
```

## 🧪 Testing

The project includes comprehensive testing with 422 test cases covering:

- API endpoint functionality
- Model validation
- Error handling
- Edge cases

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=qualer_sdk --cov-report=html

# Run specific test file
pytest tests/test_assets_api.py -v

# Run tests matching pattern
pytest tests/ -k "test_get_asset" -v
```

### Test Configuration

Tests are configured in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--strict-markers --strict-config"
```

## 🔍 Code Quality

### Code Formatting (Black)

```bash
# Format all code
black src/ tests/

# Check formatting without changes
black --check src/ tests/
```

### Linting (Flake8)

```bash
# Run linting
flake8 src/qualer_sdk

# Configuration in pyproject.toml
[tool.flake8]
max-line-length = 127
extend-ignore = ["E203", "W503"]
```

### Type Checking (MyPy)

```bash
# Run type checking
mypy src/qualer_sdk

# Configuration in pyproject.toml
[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Import Sorting (isort)

```bash
# Sort imports
isort src/ tests/

# Configuration compatible with Black
[tool.isort]
profile = "black"
```

## 🚀 CI/CD Pipeline

### GitHub Actions Workflow

The project includes a comprehensive CI/CD pipeline (`.github/workflows/ci.yml`) that:

1. **Multi-Python Testing**: Tests against Python 3.9, 3.10, 3.11, 3.12, and 3.13
2. **Code Quality Checks**: Runs linting, formatting, and type checking
3. **Test Execution**: Runs all 422 tests with coverage reporting
4. **Package Building**: Builds both source and wheel distributions
5. **Artifact Storage**: Uploads build artifacts
6. **Coverage Reporting**: Uploads coverage to Codecov

### Pipeline Triggers

- **Push**: To `master` and `develop` branches
- **Pull Requests**: To `master` and `develop` branches
- **Manual**: Can be triggered manually from GitHub Actions tab

### Pipeline Jobs

1. **test**: Multi-version testing and quality checks
2. **build**: Package building and validation
3. **publish**: Automatic PyPI publishing on tagged releases (optional)

### Status Badges

Add these badges to your README.md:

```markdown
![CI](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Johnson-Gage-Inspection-Inc/qualer-sdk-python/branch/master/graph/badge.svg)](https://codecov.io/gh/Johnson-Gage-Inspection-Inc/qualer-sdk-python)
```

## 📦 Package Management

### Building the Package

```bash
# Install build dependencies
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*
```

### Publishing to PyPI

The pipeline includes automatic publishing to PyPI when tags are pushed:

```bash
# Tag a release
git tag v1.0.0
git push origin v1.0.0
```

For manual publishing:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## 🔄 Development Workflow

### Regenerating the SDK

The SDK can be regenerated from the Qualer API's Swagger 2.0 specification:

```bash
python regenerate_sdk.py
```

The regeneration process consists of these steps:
1. Downloads the OpenAPI spec from the Qualer server
2. Patches the RecordType enum to support integer values
3. Applies fixes for multiple schema issues in the API specification using `fix_swagger_spec.py`
4. Regenerates the SDK using openapi-generator-cli
5. Post-processes the generated code (formatting, typing, etc.)

The `fix_swagger_spec.py` script specifically addresses an issue where multiple media types in the Swagger 2.0 "consumes" and "produces" arrays were causing "Multiple schemas found in the OAS 'content' section" warnings when converted to OpenAPI 3.0. The fix ensures only one media type is kept in each case.

### Feature Development

1. Create feature branch from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. Make changes and commit:
   ```bash
   # Pre-commit hooks will run automatically
   git add .
   git commit -m "feat: add new feature"
   ```

3. Push and create pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

### Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create pull request to `master`
4. After merge, tag the release:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

## 🐛 Troubleshooting

### Common Issues

1. **Pre-commit permission issues**: If pre-commit fails with permission errors, try:
   ```bash
   export PRE_COMMIT_HOME=$PWD/.pre-commit-cache
   pre-commit install
   ```

2. **Import errors**: Ensure the package is installed in development mode:
   ```bash
   pip install -e .
   ```

3. **Test failures**: Run tests with verbose output to debug:
   ```bash
   pytest tests/ -v --tb=long
   ```

### Environment Issues

- Ensure Python 3.8+ is installed
- Use virtual environments for isolation
- Keep dependencies up to date with `pip install -r requirements-dev.txt --upgrade`

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass and code quality checks succeed
6. Submit a pull request

## 🔗 Useful Links

- [GitHub Repository](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python)
- [GitHub Actions](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/actions)
- [PyPI Package](https://pypi.org/project/qualer-sdk/)
- [Documentation](./docs/)

---

This development workflow ensures code quality, reliability, and maintainability while providing a smooth developer experience.
