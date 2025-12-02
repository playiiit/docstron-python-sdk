<div align="center">
  <img height="60" src="https://docstron.com/images/png/docstron-logo.png">
  <h1 style="margin-top: 0px;">
    Docstron Python SDK
  </h1>
</div>

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Official Python SDK for the [Docstron](https://docstron.com) PDF Generation API. Generate professional PDFs from HTML templates with ease.

## Features

- ✨ **Easy to use** - Simple, intuitive API
- 🚀 **Full API coverage** - All Docstron endpoints supported
- 🔒 **Type hints** - Full typing support for better IDE integration
- 📝 **Well documented** - Comprehensive documentation and examples
- ⚡ **Async ready** - Built for modern Python applications
- 🛡️ **Error handling** - Custom exceptions for better error management

## Installation

```bash
pip install docstron
```

Or install from source:

```bash
git clone https://github.com/playiiit/docstron-python-sdk.git
cd docstron-python-sdk
pip install -e .
```

## Quick Start

```python
from docstron import Docstron

# Initialize the client
client = Docstron(api_key='your-api-key')

# Quick generate a PDF
pdf_data = client.documents.quick_generate(
    html='<h1>Hello {{name}}!</h1>',
    data={'name': 'World'},
    response_type='pdf'
)

# Save the PDF
with open('hello.pdf', 'wb') as f:
    f.write(pdf_data)
```

## Usage Examples

### Working with Applications

```python
# Get all applications
apps = client.applications.list()
for app in apps['data']:
    print(f"App: {app['name']} - {app['app_id']}")

# Get specific application
app = client.applications.get('app-7b4d78fb-820c-4ca9-84cc-46953f211234')
print(app['data'])
```

### Managing Templates

```python
# Create a template
template = client.templates.create(
    application_id='app-7b4d78fb-820c-4ca9-84cc-46953f211234',
    name='Invoice Template',
    content='''
        <html>
        <body>
            <h1>Invoice</h1>
            <p>Customer: {{customer_name}}</p>
            <p>Amount: {{amount}}</p>
            <p>Date: {{date}}</p>
        </body>
        </html>
    ''',
    extra_css='@page { margin: 2cm; }'
)

template_id = template['data']['template_id']

# List all templates
templates = client.templates.list()

# Get specific template
template = client.templates.get(template_id)

# Update template
updated = client.templates.update(
    template_id=template_id,
    name='Updated Invoice Template',
    is_active=True
)

# Delete template
client.templates.delete(template_id)
```

### Generating Documents

```python
# Generate PDF from template
pdf_binary = client.documents.generate(
    template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
    data={
        'customer_name': 'John Doe',
        'amount': '$299.00',
        'date': '2024-12-02'
    },
    response_type='pdf'
)

# Save PDF to file
with open('invoice.pdf', 'wb') as f:
    f.write(pdf_binary)

# Generate and get document ID
doc = client.documents.generate(
    template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
    data={'customer_name': 'Jane Smith', 'amount': '$599.00'},
    response_type='document_id'
)

document_id = doc['data']['document_id']

# Generate with password protection
protected_pdf = client.documents.generate(
    template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
    data={'customer_name': 'Bob Johnson'},
    response_type='pdf',
    password='secret123'
)
```

### Quick Generate (Without Template)

```python
# Generate PDF without pre-creating a template
pdf = client.documents.quick_generate(
    html='''
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; }
                .header { color: #333; }
            </style>
        </head>
        <body>
            <h1 class="header">Receipt</h1>
            <p>Thank you, {{customer}}!</p>
            <p>Total: {{total}}</p>
        </body>
        </html>
    ''',
    data={'customer': 'Alice Williams', 'total': '$49.99'},
    response_type='pdf',
    extra_css='@page { size: A4; margin: 1cm; }'
)

with open('receipt.pdf', 'wb') as f:
    f.write(pdf)

# Quick generate and save as template for future use
doc = client.documents.quick_generate(
    html='<h1>Report for {{month}}</h1>',
    data={'month': 'December'},
    save_template=True,
    application_id='app-7b4d78fb-820c-4ca9-84cc-46953f211234',
    response_type='document_id'
)
```

### Managing Documents

```python
# List all documents
docs = client.documents.list()
for doc in docs['data']:
    print(f"Document: {doc['document_id']}")

# Get specific document
doc = client.documents.get('document-517145ce-5a09-4e47-a257-887e239ecb36')
print(doc['data']['attributes'])

# Update document attributes
updated_doc = client.documents.update(
    document_id='document-517145ce-5a09-4e47-a257-887e239ecb36',
    data={'customer_name': 'Updated Name', 'amount': '$999.00'}
)

# Download document as PDF
pdf_data = client.documents.download('document-517145ce-5a09-4e47-a257-887e239ecb36')

# Or download and save directly
client.documents.download(
    'document-517145ce-5a09-4e47-a257-887e239ecb36',
    output_path='downloaded_invoice.pdf'
)

# Delete document
client.documents.delete('document-517145ce-5a09-4e47-a257-887e239ecb36')
```

### Checking Usage

```python
# Get usage statistics
usage = client.usage.get()

print(f"Plan: {usage['data']['subscription']['plan_name']}")

print(f"Documents used this month: {usage['data']['documents']['monthly']}")

print(f"Monthly limit: {usage['data']['documents']['monthly_limit']}")

print(f"Usage percentage: {usage['data']['documents']['usage_percentage']}%")

print(f"Applications: {usage['data']['applications']['total']}/{usage['data']['applications']['limit']}")

print(f"Templates: {usage['data']['templates']['total']}/{usage['data']['templates']['limit']}")
```

## Response Types

When generating documents, you can choose from three response types:

1. **`pdf`** - Returns binary PDF data directly
2. **`json_with_base64`** - Returns JSON with base64-encoded PDF
3. **`document_id`** - Returns JSON with document ID (default)

```python
# Get PDF directly
pdf = client.documents.generate(
    template_id='template-123',
    data={'name': 'Test'},
    response_type='pdf'
)

# Get base64 encoded PDF
response = client.documents.generate(
    template_id='template-123',
    data={'name': 'Test'},
    response_type='json_with_base64'
)
base64_pdf = response['data']['pdf']

# Get document ID only
response = client.documents.generate(
    template_id='template-123',
    data={'name': 'Test'},
    response_type='document_id'
)
doc_id = response['data']['document_id']
```

## Error Handling

The SDK provides custom exceptions for better error handling:

```python
from docstron import Docstron
from docstron.exceptions import (
    DocstronError,
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError
)

client = Docstron(api_key='your-api-key')

try:
    doc = client.documents.generate(
        template_id='invalid-template-id',
        data={'test': 'data'}
    )
except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
except NotFoundError as e:
    print(f"Resource not found: {e.message}")
except ValidationError as e:
    print(f"Validation error: {e.message}")
    print(f"Details: {e.response}")
except RateLimitError as e:
    print(f"Rate limit exceeded: {e.message}")
except DocstronError as e:
    print(f"An error occurred: {e.message}")
    print(f"Status code: {e.status_code}")
```

## Advanced Usage

### Custom Base URL

```python
# Use a custom API endpoint
client = Docstron(
    api_key='your-api-key',
    base_url='https://custom.docstron.com/v1'
)
```

### HTML and CSS Guidelines

For best results when creating templates:

- Use inline CSS or the `extra_css` parameter for styling
- Support for modern CSS including flexbox and grid
- Use `@page` rules in `extra_css` for page-specific styling
- Template placeholders use `{{variable_name}}` syntax

Example with advanced styling:

```python
template = client.templates.create(
    application_id='app-123',
    name='Styled Invoice',
    content='''
        <html>
        <head>
            <style>
                .container { max-width: 800px; margin: 0 auto; }
                .header { background: #1ee494; color: white; padding: 20px; }
                .content { padding: 20px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 10px; border: 1px solid #ddd; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Invoice #{{invoice_number}}</h1>
                </div>
                <div class="content">
                    <p>Customer: {{customer_name}}</p>
                    <table>
                        <tr>
                            <th>Item</th>
                            <th>Amount</th>
                        </tr>
                        <tr>
                            <td>{{item_name}}</td>
                            <td>{{item_amount}}</td>
                        </tr>
                    </table>
                </div>
            </div>
        </body>
        </html>
    ''',
    extra_css='''
        @page {
            margin: 2cm;
            @bottom-center {
                content: "Page " counter(page) " of " counter(pages);
            }
        }
    '''
)
```

## API Reference

### Client

- `Docstron(api_key, base_url='https://api.docstron.com/v1')` - Initialize client

### Applications

- `client.applications.get(app_id)` - Get application by ID
- `client.applications.list()` - List all applications

### Templates

- `client.templates.create(application_id, name, content, is_active=True, extra_css=None)` - Create template
- `client.templates.get(template_id)` - Get template by ID
- `client.templates.list()` - List all templates
- `client.templates.update(template_id, name=None, content=None, is_active=None, extra_css=None)` - Update template
- `client.templates.delete(template_id)` - Delete template

### Documents

- `client.documents.generate(template_id, data, response_type='document_id', password=None)` - Generate document
- `client.documents.quick_generate(html, data=None, response_type='document_id', extra_css=None, save_template=False, application_id=None, password=None)` - Quick generate
- `client.documents.get(document_id)` - Get document by ID
- `client.documents.list()` - List all documents
- `client.documents.update(document_id, data)` - Update document
- `client.documents.delete(document_id)` - Delete document
- `client.documents.download(document_id, output_path=None)` - Download PDF

### Usage

- `client.usage.get()` - Get usage statistics

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/playiiit/docstron-python-sdk.git
cd docstron-python-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=docstron --cov-report=html

# Run specific test file
pytest tests/test_documents.py
```

### Code Quality

```bash
# Format code
black docstron tests

# Sort imports
isort docstron tests

# Lint code
flake8 docstron tests

# Type check
mypy docstron
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📚 [Documentation](https://docs.docstron.com)
- 💬 [Issues](https://github.com/playiiit/docstron-python-sdk/issues)
- 📧 Email: support@docstron.com

## Links

- [Docstron Website](https://docstron.com)
- [API Documentation](https://docs.docstron.com)
- [GitHub Repository](https://github.com/playiiit/docstron-python-sdk)

---

Made with ❤️ by [Playiiit Company](https://playiiit.com)
