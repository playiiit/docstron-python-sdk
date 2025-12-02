"""
Test configuration
"""

import pytest


@pytest.fixture
def mock_api_key():
    """Fixture for mock API key"""
    return 'test-api-key-12345'


@pytest.fixture
def mock_app_id():
    """Fixture for mock application ID"""
    return 'app-7b4d78fb-820c-4ca9-84cc-46953f211234'


@pytest.fixture
def mock_template_id():
    """Fixture for mock template ID"""
    return 'template-c2465c0b-fc54-4672-b9ac-7446886cd6de'


@pytest.fixture
def mock_document_id():
    """Fixture for mock document ID"""
    return 'document-517145ce-5a09-4e47-a257-887e239ecb36'
