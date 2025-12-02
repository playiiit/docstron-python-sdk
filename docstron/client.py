"""
Main Docstron client
"""

from .base import BaseClient
from .resources import Applications, Templates, Documents, Usage


class Docstron(BaseClient):
    """
    Main client for the Docstron API
    
    Args:
        api_key: Your Docstron API key
        base_url: Base URL for the API (default: https://api.docstron.com/v1)
    
    Example:
        >>> from docstron import Docstron
        >>> client = Docstron(api_key='your-api-key')
        
        >>> # Work with applications
        >>> apps = client.applications.list()
        
        >>> # Create a template
        >>> template = client.templates.create(
        ...     application_id='app-123',
        ...     name='Invoice',
        ...     content='<h1>Invoice for {{customer}}</h1>'
        ... )
        
        >>> # Generate a PDF
        >>> pdf = client.documents.generate(
        ...     template_id=template['data']['template_id'],
        ...     data={'customer': 'Acme Corp'},
        ...     response_type='pdf'
        ... )
        
        >>> # Check usage
        >>> usage = client.usage.get()
    """

    def __init__(self, api_key: str, base_url: str = "https://api.docstron.com/v1"):
        super().__init__(api_key, base_url)
        
        # Initialize resource classes
        self.applications = Applications(self)
        self.templates = Templates(self)
        self.documents = Documents(self)
        self.usage = Usage(self)
