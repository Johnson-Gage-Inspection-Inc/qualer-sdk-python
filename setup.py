from setuptools import find_packages, setup

setup(
    author="Johnson Gage & Inspection Inc.",
    author_email="jhall@jgiquality.com",
    description="Auto-generated Python client for Qualer",
    include_package_data=True,
    install_requires=["urllib3>=1.15", "six>=1.10", "certifi", "python-dateutil"],
    name="qualer-sdk",
    package_data={"": ["py.typed"]},
    package_dir={"": "qualer_sdk"},
    packages=find_packages(where="qualer_sdk"),
    python_requires=">=3.7",
    version="2.2.1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
