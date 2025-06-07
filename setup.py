from setuptools import find_packages, setup

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qualer-sdk",
    version="2.2.1",
    description="Auto-generated Python client for Qualer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Johnson Gage & Inspection Inc.",
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
        "pydantic>=2.11.0,<2.12.0",
    ],    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
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
