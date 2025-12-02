"""
Unit tests for the Docstron client
"""

import pytest
from docstron import Docstron
from docstron.resources import Applications, Templates, Documents, Usage


class TestDocstronClient:
    """Test the main Docstron client"""

    def test_client_initialization(self):
        """Test client initialization"""
        client = Docstron(api_key='test-key')
        assert client.api_key == 'test-key'
        assert client.base_url == 'https://api.docstron.com/v1'

    def test_client_custom_base_url(self):
        """Test client with custom base URL"""
        custom_url = 'https://custom.api.com/v1'
        client = Docstron(api_key='test-key', base_url=custom_url)
        assert client.base_url == custom_url

    def test_client_resources(self):
        """Test that all resources are initialized"""
        client = Docstron(api_key='test-key')
        assert isinstance(client.applications, Applications)
        assert isinstance(client.templates, Templates)
        assert isinstance(client.documents, Documents)
        assert isinstance(client.usage, Usage)

    def test_client_headers(self):
        """Test that headers are set correctly"""
        client = Docstron(api_key='test-key-123')
        assert client.session.headers['Authorization'] == 'Bearer test-key-123'
        assert client.session.headers['Content-Type'] == 'application/json'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
