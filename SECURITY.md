# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please email us at security@docstron.com.

**Please do not report security vulnerabilities through public GitHub issues.**

We will respond to your report within 48 hours and work with you to understand and resolve the issue.

## What to Include

When reporting a vulnerability, please include:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Suggested fix (if you have one)

## Security Best Practices

When using the Docstron SDK:

1. **Never commit API keys** to version control
2. **Use environment variables** to store API keys
3. **Rotate API keys** regularly
4. **Use HTTPS** for all API communications (SDK default)
5. **Validate user input** before passing to templates
6. **Monitor usage** to detect unusual activity

## Example: Secure API Key Storage

```python
import os
from docstron import Docstron

# Good: Use environment variable
api_key = os.getenv('DOCSTRON_API_KEY')
client = Docstron(api_key=api_key)

# Bad: Hardcoded API key
# client = Docstron(api_key='your-api-key-here')  # Don't do this!
```
