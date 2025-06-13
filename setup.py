from setuptools import find_packages, setup
from setuptools_scm import get_version  # noqa: F401

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qualer-sdk",
    use_scm_version={
        "version_scheme": "python-simplified-semver",
        "local_scheme": "node-and-date",
        "tag_regex": r"^v(?P<version>.*)$",
    },
    setup_requires=["setuptools-scm"],
    description="Auto-generated Python client for Qualer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jeff Hall",
    author_email="jhall@jgiquality.com",
    url="https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"qualer_sdk": ["py.typed"]},
    install_requires=[
        "urllib3>=1.15",
        "six>=1.10",
        "certifi",
        "python-dateutil",
        "attrs>=21.3.0",
        "httpx>=0.20.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    keywords="qualer api sdk client",
    project_urls={
        "Bug Reports": "https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/issues",
        "Source": "https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python",
    },
)
