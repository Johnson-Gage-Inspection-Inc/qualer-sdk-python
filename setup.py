from setuptools import find_packages, setup

setup(
    name="qualer-sdk",
    version="2.2.1",
    description="Auto-generated Python client for Qualer",
    author="Johnson Gage & Inspection Inc.",
    author_email="jhall@jgiquality.com",
    packages=find_packages(where="qualer_sdk"),
    package_dir={"": "qualer_sdk"},
    install_requires=["urllib3>=1.15", "six>=1.10", "certifi", "python-dateutil"],
    python_requires=">=3.7",
    include_package_data=True,
    package_data={"qualer_sdk": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
