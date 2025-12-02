# Changelog

All notable changes to the Docstron Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-02

### Added
- Initial release of Docstron Python SDK
- Support for all Docstron API endpoints
- Applications resource (get, list)
- Templates resource (create, get, list, update, delete)
- Documents resource (generate, quick_generate, get, list, update, delete, download)
- Usage resource (get statistics)
- Custom exception classes for better error handling
- Type hints for all methods
- Comprehensive documentation and examples
- Unit tests
- Support for password-protected PDFs
- Support for custom CSS styling
- Three response types for document generation (pdf, json_with_base64, document_id)
- Automatic file saving for document downloads

### Security
- Secure API key handling via Bearer token authentication
- HTTPS-only communication with Docstron API

[1.0.0]: https://github.com/playiiit/docstron-python-sdk/releases/tag/v1.0.0
