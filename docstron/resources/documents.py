"""
Documents resource for the Docstron API
"""

from typing import Dict, Any, List, Optional, Literal


class Documents:
    """Manage Docstron documents"""

    def __init__(self, client):
        self._client = client

    def generate(
        self,
        template_id: str,
        data: Dict[str, Any],
        response_type: Literal["pdf", "json_with_base64", "document_id"] = "document_id",
        password: Optional[str] = None,
    ) -> Dict[str, Any] | bytes:
        """
        Generate a document from a template

        Args:
            template_id: The template ID to use for generation
            data: Dictionary of data to fill template placeholders
            response_type: Type of response:
                - 'pdf': Returns PDF file directly (binary)
                - 'json_with_base64': Returns JSON with base64 encoded PDF
                - 'document_id': Returns JSON with document ID (default)
            password: Optional password to protect the PDF

        Returns:
            Depends on response_type:
            - 'pdf': Binary PDF data
            - 'json_with_base64': Dict with base64 PDF
            - 'document_id': Dict with document ID

        Example:
            >>> # Generate and get document ID
            >>> doc = client.documents.generate(
            ...     template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
            ...     data={'customer_name': 'John Doe', 'amount': '$299.00'},
            ...     response_type='document_id'
            ... )
            
            >>> # Generate and get PDF directly
            >>> pdf_data = client.documents.generate(
            ...     template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
            ...     data={'customer_name': 'John Doe'},
            ...     response_type='pdf'
            ... )
            >>> with open('output.pdf', 'wb') as f:
            ...     f.write(pdf_data)
        """
        payload = {
            "template_id": template_id,
            "data": data,
            "response_type": response_type,
        }
        if password:
            payload["password"] = password

        if response_type == "pdf":
            # For PDF response, we need to POST the data and get binary response
            return self._client.post_binary("documents/generate", data=payload)
        else:
            response = self._client.post("documents/generate", data=payload)
            return response

    def quick_generate(
        self,
        html: str,
        data: Optional[Dict[str, Any]] = None,
        response_type: Literal["pdf", "json_with_base64", "document_id"] = "document_id",
        extra_css: Optional[str] = None,
        save_template: bool = False,
        application_id: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any] | bytes:
        """
        Generate a document without pre-creating a template

        Args:
            html: HTML content with optional placeholders
            data: Dictionary of data to fill placeholders (optional)
            response_type: Type of response ('pdf', 'json_with_base64', 'document_id')
            extra_css: Optional CSS styles
            save_template: Whether to save this as a template (default: False)
            application_id: Required if save_template is True
            password: Optional password to protect the PDF

        Returns:
            Depends on response_type (same as generate method)

        Example:
            >>> # Quick generate without saving template
            >>> doc = client.documents.quick_generate(
            ...     html='<h1>Hello {{name}}</h1>',
            ...     data={'name': 'World'},
            ...     response_type='pdf'
            ... )
            
            >>> # Quick generate and save as template
            >>> doc = client.documents.quick_generate(
            ...     html='<h1>Invoice for {{customer}}</h1>',
            ...     data={'customer': 'Acme Corp'},
            ...     save_template=True,
            ...     application_id='app-7b4d78fb-820c-4ca9-84cc-46953f211234'
            ... )
        """
        payload = {
            "html": html,
            "response_type": response_type,
            "save_template": save_template,
        }
        if data:
            payload["data"] = data
        if extra_css:
            payload["extra_css"] = extra_css
        if save_template and application_id:
            payload["application_id"] = application_id
        if password:
            payload["password"] = password

        if response_type == "pdf":
            # For PDF response, we need to POST the data and get binary response
            return self._client.post_binary("documents/quick/generate", data=payload)
        else:
            response = self._client.post("documents/quick/generate", data=payload)
            return response

    def get(self, document_id: str) -> Dict[str, Any]:
        """
        Get a specific document by ID

        Args:
            document_id: The document ID

        Returns:
            Dictionary containing document details

        Example:
            >>> doc = client.documents.get('document-517145ce-5a09-4e47-a257-887e239ecb36')
            >>> print(doc['data']['attributes'])
        """
        response = self._client.get(f"documents/{document_id}")
        return response

    def list(self) -> List[Dict[str, Any]]:
        """
        Get all documents

        Returns:
            List of dictionaries containing document details

        Example:
            >>> docs = client.documents.list()
            >>> for doc in docs['data']:
            ...     print(doc['document_id'])
        """
        response = self._client.get("documents")
        return response

    def update(
        self, document_id: str, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update a document's attributes

        Note: This updates the stored data/attributes, not the PDF itself.
        To regenerate the PDF, use the generate method.

        Args:
            document_id: The document ID to update
            data: New data/attributes for the document

        Returns:
            Dictionary containing the updated document details

        Example:
            >>> doc = client.documents.update(
            ...     document_id='document-517145ce-5a09-4e47-a257-887e239ecb36',
            ...     data={'customer_name': 'Jane Doe', 'amount': '$399.00'}
            ... )
        """
        payload = {"data": data}
        response = self._client.patch(f"documents/{document_id}", data=payload)
        return response

    def delete(self, document_id: str) -> Dict[str, Any]:
        """
        Delete a document

        Args:
            document_id: The document ID to delete

        Returns:
            Dictionary containing the deletion result

        Example:
            >>> result = client.documents.delete('document-517145ce-5a09-4e47-a257-887e239ecb36')
        """
        response = self._client.delete(f"documents/{document_id}")
        return response

    def download(self, document_id: str, output_path: Optional[str] = None) -> bytes:
        """
        Download a document as PDF

        Args:
            document_id: The document ID to download
            output_path: Optional path to save the PDF file

        Returns:
            Binary PDF data

        Example:
            >>> # Download and get binary data
            >>> pdf_data = client.documents.download('document-489a79af-8680-4a08-a777-df52f26f296f')
            
            >>> # Download and save to file
            >>> client.documents.download(
            ...     'document-489a79af-8680-4a08-a777-df52f26f296f',
            ...     output_path='invoice.pdf'
            ... )
        """
        pdf_data = self._client.download(f"documents/download/{document_id}")
        
        if output_path:
            with open(output_path, "wb") as f:
                f.write(pdf_data)
        
        return pdf_data
