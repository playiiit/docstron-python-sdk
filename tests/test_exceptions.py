"""
Unit tests for exception handling
"""

import pytest
from docstron.exceptions import (
    DocstronError,
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError,
)


class TestExceptions:
    """Test custom exceptions"""

    def test_docstron_error_basic(self):
        """Test basic DocstronError"""
        error = DocstronError('Test error')
        assert str(error) == 'Test error'
        assert error.message == 'Test error'
        assert error.status_code is None
        assert error.response is None

    def test_docstron_error_with_details(self):
        """Test DocstronError with status code and response"""
        response = {'error': 'details'}
        error = DocstronError('Test error', status_code=400, response=response)
        assert error.message == 'Test error'
        assert error.status_code == 400
        assert error.response == response

    def test_authentication_error(self):
        """Test AuthenticationError"""
        error = AuthenticationError('Invalid API key', status_code=401)
        assert isinstance(error, DocstronError)
        assert error.message == 'Invalid API key'
        assert error.status_code == 401

    def test_not_found_error(self):
        """Test NotFoundError"""
        error = NotFoundError('Resource not found', status_code=404)
        assert isinstance(error, DocstronError)
        assert error.status_code == 404

    def test_validation_error(self):
        """Test ValidationError"""
        error = ValidationError('Invalid input', status_code=422)
        assert isinstance(error, DocstronError)
        assert error.status_code == 422

    def test_rate_limit_error(self):
        """Test RateLimitError"""
        error = RateLimitError('Too many requests', status_code=429)
        assert isinstance(error, DocstronError)
        assert error.status_code == 429

    def test_server_error(self):
        """Test ServerError"""
        error = ServerError('Internal server error', status_code=500)
        assert isinstance(error, DocstronError)
        assert error.status_code == 500


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
