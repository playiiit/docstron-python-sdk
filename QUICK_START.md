# Docstron Python SDK - Quick Setup Guide

## 📦 Installation

### Option 1: Install from PyPI (Once Published)
```bash
pip install docstron
```

### Option 2: Install from Source
```bash
# Clone the repository
git clone https://github.com/playiiit/docstron-python-sdk.git
cd docstron-python-sdk

# Install in development mode
pip install -e .
```

### Option 3: Install for Development
```bash
# Install with development dependencies
pip install -e ".[dev]"
```

## 🚀 Quick Start

```python
from docstron import Docstron

# Initialize the client with your API key
client = Docstron(api_key='your-api-key')

# Generate a PDF
pdf = client.documents.quick_generate(
    html='<h1>Hello {{name}}!</h1>',
    data={'name': 'World'},
    response_type='pdf'
)

# Save the PDF
with open('hello.pdf', 'wb') as f:
    f.write(pdf)
```

## 📂 Project Structure

```
docstron-python-sdk/
│
├── docstron/                    # Main package
│   ├── __init__.py             # Package exports
│   ├── client.py               # Main Docstron client
│   ├── base.py                 # Base HTTP client
│   ├── exceptions.py           # Custom exceptions
│   └── resources/              # API resource classes
│       ├── __init__.py
│       ├── applications.py     # Applications API
│       ├── templates.py        # Templates API
│       ├── documents.py        # Documents API
│       └── usage.py            # Usage API
│
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── conftest.py            # Test configuration
│   ├── test_client.py         # Client tests
│   └── test_exceptions.py     # Exception tests
│
├── examples/                   # Usage examples
│   ├── README.md
│   ├── 01_quick_start.py
│   ├── 02_invoice_template.py
│   ├── 03_error_handling.py
│   └── 04_managing_resources.py
│
├── setup.py                    # Package setup
├── pyproject.toml             # Build configuration
├── requirements.txt           # Core dependencies
├── requirements-dev.txt       # Dev dependencies
├── README.md                  # Main documentation
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # Contribution guidelines
├── SECURITY.md               # Security policy
├── LICENSE                   # MIT License
├── MANIFEST.in              # Package manifest
└── .gitignore               # Git ignore rules
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=docstron --cov-report=html

# Run specific test file
pytest tests/test_client.py -v
```

## 🎨 Code Quality

```bash
# Format code
black docstron tests

# Sort imports
isort docstron tests

# Lint code
flake8 docstron tests

# Type checking
mypy docstron
```

## 📖 API Overview

### Client Initialization
```python
from docstron import Docstron

client = Docstron(api_key='your-api-key')
```

### Applications
```python
# List all applications
apps = client.applications.list()

# Get specific application
app = client.applications.get('app-id')
```

### Templates
```python
# Create template
template = client.templates.create(
    application_id='app-id',
    name='My Template',
    content='<h1>{{title}}</h1>'
)

# List templates
templates = client.templates.list()

# Update template
client.templates.update(template_id='template-id', name='Updated Name')

# Delete template
client.templates.delete('template-id')
```

### Documents
```python
# Generate from template
pdf = client.documents.generate(
    template_id='template-id',
    data={'title': 'Hello'},
    response_type='pdf'
)

# Quick generate (no template needed)
pdf = client.documents.quick_generate(
    html='<h1>{{title}}</h1>',
    data={'title': 'Hello'},
    response_type='pdf'
)

# Download document
client.documents.download('doc-id', output_path='file.pdf')

# List documents
docs = client.documents.list()

# Update document
client.documents.update('doc-id', data={'new': 'data'})

# Delete document
client.documents.delete('doc-id')
```

### Usage Statistics
```python
# Get usage info
usage = client.usage.get()
print(f"Documents used: {usage['data']['documents']['monthly']}")
```

## 🔑 Environment Variables

For security, use environment variables for your API key:

```bash
# .env file
DOCSTRON_API_KEY=your-api-key-here
```

```python
import os
from docstron import Docstron

client = Docstron(api_key=os.getenv('DOCSTRON_API_KEY'))
```

## 🐛 Error Handling

```python
from docstron import Docstron
from docstron.exceptions import (
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    DocstronError
)

try:
    doc = client.documents.generate(...)
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Resource not found")
except ValidationError as e:
    print(f"Invalid input: {e.message}")
except RateLimitError:
    print("Rate limit exceeded")
except DocstronError as e:
    print(f"Error: {e.message}")
```

## 📦 Building the Package

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# - dist/docstron-1.0.0.tar.gz
# - dist/docstron-1.0.0-py3-none-any.whl
```

## 🚢 Publishing to PyPI

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*
```

## 🔗 Resources

- **API Documentation**: https://docs.docstron.com
- **GitHub Repository**: https://github.com/playiiit/docstron-python-sdk
- **PyPI Package**: https://pypi.org/project/docstron/
- **Support**: support@docstron.com

## 📝 Next Steps

1. **Get your API key** from https://app.docstron.com
2. **Install the SDK**: `pip install docstron`
3. **Try the examples** in the `examples/` directory
4. **Read the docs** at https://docs.docstron.com
5. **Build something amazing!** 🚀

---

### Features Implemented

✅ Full API coverage (Applications, Templates, Documents, Usage)  
✅ Type hints for better IDE support  
✅ Custom exception handling  
✅ Response type options (pdf, json_with_base64, document_id)  
✅ Password-protected PDF generation  
✅ Custom CSS styling support  
✅ File download helpers  
✅ Comprehensive documentation  
✅ Usage examples  
✅ Unit tests  
✅ PyPI-ready packaging  

### SDK Highlights

- **Simple & Intuitive**: Easy-to-use API that follows Python best practices
- **Production Ready**: Full error handling, type hints, and tests
- **Well Documented**: Comprehensive README, examples, and docstrings
- **Flexible**: Multiple response types and customization options
- **Secure**: Best practices for API key management

Enjoy using the Docstron Python SDK! 🎉
