import os

from setuptools import find_packages, setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="naboopay",
    version="1.0.0",
    author="sudoping01",
    author_email="sudoping01@gmail.com",
    description="NabooPay Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudoping01/naboopay",
    project_urls={
        "Bug Tracker": " https://github.com/naboopay/naboopay-python-sdk/issues",
        "Documentation": " https://github.com/naboopay/naboopay-python-sdk.git",
        "Source Code": "https://github.com/sudoping01/naboopay",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "aiohttp>=3.8.0",
        "pydantic>=1.8.0,<2.0.0",
        "tenacity>=9.1.2",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.18.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
            "black>=23.0.0",
            "isort>=5.0.0",
            "ruff>=0.11.4",
            "pre-commit>=2.15.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
    },
    keywords=[
        "naboopay",
        "payment",
        "gateway",
        "senegal",
        "mobile money",
        "wave",
        "orange money",
        "api",
        "sdk",
        "fintech",
    ],
    include_package_data=True,
    zip_safe=False,
)
