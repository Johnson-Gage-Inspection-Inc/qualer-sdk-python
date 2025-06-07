import os
import re
import sys

from setuptools import find_packages

# Add the parent directory to sys.path to allow importing setup.py as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))


def test_readme_exists():
    """Test that README.md file exists"""
    assert os.path.isfile("README.md"), "README.md file not found"


def test_setup_version_format():
    """Test that version follows semantic versioning"""
    with open("setup.py", "r", encoding="utf-8") as f:
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
    assert os.path.isdir("src"), "src directory not found"
    packages = find_packages(where="src")
    assert "qualer_sdk" in packages, "qualer_sdk package not found in src directory"


def test_required_dependencies():
    """Test that all required dependencies are listed"""
    required_deps = ["urllib3", "six", "certifi", "python-dateutil"]

    with open("setup.py", "r", encoding="utf-8") as f:
        content = f.read()

    for dep in required_deps:
        assert dep in content, f"Required dependency {dep} not found in setup.py"


def test_python_version_requirement():
    """Test that python_requires is set to >=3.7"""
    with open("setup.py", "r", encoding="utf-8") as f:
        content = f.read()

    assert (
        'python_requires=">=3.7"' in content
    ), "Python version requirement should be >=3.7"


def test_package_data():
    """Test that py.typed is included in package data"""
    with open("setup.py", "r", encoding="utf-8") as f:
        content = f.read()

    assert (
        'package_data={"qualer_sdk": ["py.typed"]}' in content
    ), "py.typed should be included in package data"


def test_classifiers():
    """Test that important classifiers are included"""
    with open("setup.py", "r", encoding="utf-8") as f:
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
        assert (
            classifier in content
        ), f"Important classifier '{classifier}' not found in setup.py"
