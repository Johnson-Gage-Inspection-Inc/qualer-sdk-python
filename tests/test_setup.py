import os
import re
import sys

from setuptools import find_packages

# Add the repository root directory to sys.path to allow importing setup.py as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_readme_exists():
    """Test that README.md file exists"""
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    assert os.path.isfile(readme_path), "README.md file not found"


def test_setup_version_format():
    """Test that version follows semantic versioning"""
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract version using regex
    version_match = re.search(r'version="([^"]+)"', content)
    assert version_match, "Version not found in setup.py"

    version = version_match.group(1)
    # Check semantic versioning pattern (MAJOR.MINOR.PATCH)
    assert re.match(
        r"^\d+\.\d+\.\d+$", version
    ), f"Version {version} doesn't follow semantic versioning"


def test_package_structure():
    """Test that src directory exists and contains packages"""
    src_path = os.path.join(os.path.dirname(__file__), "..", "src")
    assert os.path.isdir(src_path), "src directory not found"
    packages = find_packages(where=src_path)
    assert "qualer_sdk" in packages, "qualer_sdk package not found in src directory"


def test_required_dependencies():
    """Test that all required dependencies are listed"""
    required_deps = ["urllib3", "six", "certifi", "python-dateutil"]

    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    for dep in required_deps:
        assert dep in content, f"Required dependency {dep} not found in setup.py"


def test_python_version_requirement():
    """Test that python_requires is set to >=3.9"""
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert (
        'python_requires=">=3.9"' in content
    ), "Python version requirement should be >=3.9"


def test_package_data():
    """Test that py.typed is included in package data"""
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert (
        'package_data={"qualer_sdk": ["py.typed"]}' in content
    ), "py.typed should be included in package data"


def test_classifiers():
    """Test that important classifiers are included"""
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    important_classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Typing :: Typed",
    ]

    for classifier in important_classifiers:
        assert (
            classifier in content
        ), f"Important classifier '{classifier}' not found in setup.py"
