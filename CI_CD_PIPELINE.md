# CI/CD Pipeline Documentation

## 🚀 Overview

The Qualer SDK Python project uses a comprehensive CI/CD pipeline that includes testing, building, and publishing workflows.

## 📋 Pipeline Structure

### 1. **CI Pipeline** (`.github/workflows/ci.yml`)

Triggered on: **Pull Requests to `master`**

#### Jobs:

**🧪 Test Job**
- **Matrix Testing**: Python 3.9, 3.10, 3.11, 3.12
- **Dependency Caching**: Speeds up builds
- **Linting**: flake8 for code quality
- **SDK Validation**: Import tests
- **Unit Tests**: pytest with coverage
- **Coverage Upload**: Codecov integration

**🔍 CodeQL Analysis**
- **Security Scanning**: GitHub's CodeQL
- **Vulnerability Detection**: Automated security analysis

**📦 Build Job**
- **Dynamic Versioning**: setuptools-scm validation
- **Package Building**: Both wheel and sdist
- **Package Integrity**: twine check
- **Installation Testing**: Verify wheel installs correctly
- **Artifact Upload**: Store built packages

### 2. **Publish Pipeline** (`.github/workflows/publish.yml`)

Triggered on: **Git tags** (e.g., `v3.0.0`, `v3.1.0`)

#### Features:

**🔖 Version Verification**
- Ensures Git tag matches package version
- Prevents accidental version mismatches

**📦 Package Building & Testing**
- Full build and integrity checks
- Installation verification

**🚀 PyPI Publishing**
- **Trusted Publishing**: Secure, token-free deployment
- **Environment Protection**: Uses GitHub environments
- **Artifact Storage**: Preserves distributions

## 🎯 Why Build Wheels in CI?

### ✅ **Quality Assurance**

1. **🔍 Build Validation**: Ensures packages build on clean environments
2. **📦 Distribution Testing**: Validates packaging configuration
3. **🔧 Dependency Resolution**: Catches dependency issues early
4. **⚙️ setuptools-scm Verification**: Tests dynamic versioning

### ✅ **Security & Reliability**

1. **🛡️ Reproducible Builds**: Same environment every time
2. **🔒 Supply Chain Security**: Verified build process
3. **📝 Audit Trail**: Complete build history
4. **🚫 Human Error Prevention**: Automated process reduces mistakes

### ✅ **Developer Experience**

1. **⚡ Fast Feedback**: Quick detection of packaging issues
2. **🔄 Continuous Integration**: Seamless development workflow
3. **📊 Coverage Reports**: Automated test coverage tracking
4. **🏷️ Artifact Storage**: Easy access to built packages

## 🛠️ Key Improvements Made

### **Enhanced Build Job**

```yaml
- name: Verify dynamic versioning
  run: |
    python -c "import setuptools_scm; print(f'📦 Version: {setuptools_scm.get_version()}')"

- name: Test installation from wheel
  run: |
    pip install dist/*.whl
    python -c "import qualer_sdk; print(f'✅ Installed version: {qualer_sdk.__version__}')"
```

### **Version Verification**

```yaml
- name: Verify version matches tag
  run: |
    TAG_VERSION=${GITHUB_REF#refs/tags/v}
    SCM_VERSION=$(python -c "import setuptools_scm; print(setuptools_scm.get_version())")
    # Verify versions match
```

### **Trusted Publishing**

```yaml
- name: Publish to PyPI (Trusted Publishing)
  uses: pypa/gh-action-pypi-publish@release/v1
```

## 🚀 Publishing Workflow

### **Automatic Publishing**

1. **Create Git Tag**: `git tag v3.1.0 && git push origin v3.1.0`
2. **Automatic Trigger**: Publish workflow starts
3. **Build & Test**: Package is built and tested
4. **Version Verification**: Ensures tag matches package version
5. **PyPI Upload**: Automatic publishing to PyPI

### **Manual Override**

The publish workflow is currently set to build and test but not automatically publish (commented out). To enable:

1. Set up PyPI trusted publishing or add `PYPI_API_TOKEN` secret
2. Uncomment the publishing step
3. Configure GitHub environment protection (recommended)

## 🔧 Local Development

### **Build Locally**
```bash
# Install build tools
pip install build twine setuptools-scm

# Build package
python -m build

# Check package
twine check dist/*

# Test installation
pip install dist/*.whl
```

### **Version Check**
```bash
# Check current version
python show_version.py

# Verify setuptools-scm
python -c "import setuptools_scm; print(setuptools_scm.get_version())"
```

## 📈 Benefits for Qualer SDK

1. **🔄 Automated Quality**: Every PR is tested and built
2. **📦 Reliable Releases**: Consistent package generation
3. **🛡️ Security**: Secure publishing process
4. **⚡ Fast Iteration**: Quick feedback on changes
5. **📊 Visibility**: Clear build status and coverage metrics
6. **🎯 Professional**: Production-ready CI/CD pipeline

The wheel building in CI is essential for maintaining package quality, security, and developer productivity. It catches issues early and ensures reliable distributions.
