Contributing to NabooPay Python SDK
Thank you for your interest in contributing to the NabooPay Python SDK! We welcome contributions from the community to enhance this payment gateway SDK.
Table of Contents

Setting Up the Development Environment
Coding Standards
Running Tests
Submitting Pull Requests


Setting Up the Development Environment

Clone the Repository  
git clone https://github.com/naboopay/naboopay-python-sdk.git
cd naboopay-python-sdk


Install DependenciesInstall development dependencies listed in dev-requirements.txt:  
pip install -r dev-requirements.txt


Set Up Pre-Commit HooksEnsure code quality with pre-commit hooks:  
pre-commit install




Coding Standards

Adhere to PEP 8 for Python code style.  
Use descriptive variable and function names.  
Include docstrings for all public classes and methods.  
Format code with black and sort imports with isort.


Running Tests
Run the test suite to verify your changes:  
pytest test/

All tests must pass before submitting a pull request.

Submitting Pull Requests

Fork the repository and create a feature or bug-fix branch.  
Make changes following the Coding Standards.  
Add tests for new features or fixes.  
Run tests and ensure they pass.  
Commit with a clear message (e.g., "Add support for X feature").  
Push your branch and submit a pull request to the main repository.

Follow the template when submitting your pull request.
