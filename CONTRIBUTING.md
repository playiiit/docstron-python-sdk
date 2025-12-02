# Contributing to Docstron Python SDK

Thank you for your interest in contributing to the Docstron Python SDK! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Code samples** if applicable
- **Environment details** (Python version, OS, SDK version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the enhancement
- **Use case** explaining why it would be useful
- **Possible implementation** approach if you have ideas

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for any new functionality
4. **Update documentation** if needed
5. **Ensure tests pass** by running `pytest`
6. **Format your code** using `black` and `isort`
7. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/docstron-python-sdk.git
cd docstron-python-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

## Coding Standards

### Style Guide

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black default)
- Use type hints for function parameters and return values

### Code Formatting

```bash
# Format code with Black
black docstron tests

# Sort imports with isort
isort docstron tests

# Check for issues with flake8
flake8 docstron tests

# Type check with mypy
mypy docstron
```

### Testing

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow existing test patterns

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=docstron --cov-report=html

# Run specific test file
pytest tests/test_client.py -v
```

### Documentation

- Add docstrings to all public classes and methods
- Follow Google or NumPy docstring style
- Include examples in docstrings where helpful
- Update README.md for significant changes

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable

Examples:
```
Add support for custom timeout configuration
Fix template update method parameter validation
Update documentation for quick_generate method
```

## Project Structure

```
docstron-python-sdk/
├── docstron/              # Main package
│   ├── __init__.py       # Package initialization
│   ├── client.py         # Main client class
│   ├── base.py           # Base HTTP client
│   ├── exceptions.py     # Custom exceptions
│   └── resources/        # Resource classes
│       ├── __init__.py
│       ├── applications.py
│       ├── templates.py
│       ├── documents.py
│       └── usage.py
├── tests/                # Unit tests
├── examples/             # Usage examples
├── setup.py             # Package setup
├── pyproject.toml       # Build configuration
└── README.md            # Main documentation
```

## Adding New Features

When adding new features:

1. **Check the API documentation** at https://docs.docstron.com
2. **Create a new branch** for your feature
3. **Implement the feature** in the appropriate resource class
4. **Add comprehensive tests** covering success and error cases
5. **Update documentation** including README examples
6. **Create an example file** in `examples/` if applicable

## Release Process

Maintainers will handle releases. The process includes:

1. Update version in `setup.py`, `pyproject.toml`, and `__init__.py`
2. Update `CHANGELOG.md` with changes
3. Create a git tag for the version
4. Build and publish to PyPI
5. Create a GitHub release

## Questions?

If you have questions about contributing:

- Check existing [issues](https://github.com/playiiit/docstron-python-sdk/issues)
- Create a new issue with the `question` label
- Email: support@docstron.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Docstron Python SDK! 🎉
