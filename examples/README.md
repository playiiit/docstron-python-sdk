# Docstron Python SDK Examples

This directory contains examples demonstrating how to use the Docstron Python SDK.

## Prerequisites

Before running these examples, make sure you have:

1. Installed the Docstron SDK:
   ```bash
   pip install docstron
   ```

2. Obtained your API key from [Docstron Dashboard](https://app.docstron.com)

3. Replaced `'your-api-key-here'` in the examples with your actual API key

## Examples

### 01_quick_start.py
The simplest way to generate a PDF. Perfect for getting started quickly.

```bash
python 01_quick_start.py
```

### 02_invoice_template.py
Demonstrates creating a professional invoice template and generating a PDF from it.

```bash
python 02_invoice_template.py
```

### 03_error_handling.py
Shows how to handle different types of errors and implement retry logic.

```bash
python 03_error_handling.py
```

### 04_managing_resources.py
Comprehensive example covering all resource operations (CRUD for templates, documents, etc.).

```bash
python 04_managing_resources.py
```

## Tips

- Always store your API key securely (use environment variables in production)
- Check your usage limits with `client.usage.get()`
- Use `response_type='pdf'` for direct PDF download
- Use `response_type='document_id'` to save document metadata for later retrieval

## Getting Help

- [Documentation](https://docs.docstron.com)
- [API Reference](https://docs.docstron.com/api-reference)
- [GitHub Issues](https://github.com/playiiit/docstron-python-sdk/issues)
