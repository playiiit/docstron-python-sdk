"""
Templates resource for the Docstron API
"""

from typing import Dict, Any, List, Optional


class Templates:
    """Manage Docstron templates"""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        application_id: str,
        name: str,
        content: str,
        is_active: bool = True,
        extra_css: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a new template

        Args:
            application_id: The ID of the application this template belongs to
            name: Template name
            content: HTML content with placeholders (e.g., '{{variable_name}}')
            is_active: Whether the template is active (default: True)
            extra_css: Optional CSS styles for PDF generation

        Returns:
            Dictionary containing the created template details

        Example:
            >>> template = client.templates.create(
            ...     application_id='app-7b4d78fb-820c-4ca9-84cc-46953f211234',
            ...     name='Invoice Template',
            ...     content='<h1>Invoice for {{customer_name}}</h1>',
            ...     extra_css='@page { margin: 3cm; }'
            ... )
        """
        data = {
            "application_id": application_id,
            "name": name,
            "content": content,
            "is_active": is_active,
        }
        if extra_css:
            data["extra_css"] = extra_css

        response = self._client.post("templates", data=data)
        return response

    def get(self, template_id: str) -> Dict[str, Any]:
        """
        Get a specific template by ID

        Args:
            template_id: The template ID

        Returns:
            Dictionary containing template details

        Example:
            >>> template = client.templates.get('template-c2465c0b-fc54-4672-b9ac-7446886cd6de')
        """
        response = self._client.get(f"templates/{template_id}")
        return response

    def list(self) -> List[Dict[str, Any]]:
        """
        Get all templates

        Returns:
            List of dictionaries containing template details

        Example:
            >>> templates = client.templates.list()
            >>> for template in templates['data']:
            ...     print(template['name'])
        """
        response = self._client.get("templates")
        return response

    def update(
        self,
        template_id: str,
        name: Optional[str] = None,
        content: Optional[str] = None,
        is_active: Optional[bool] = None,
        extra_css: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update a template

        Args:
            template_id: The template ID to update
            name: New template name (optional)
            content: New HTML content (optional)
            is_active: New active status (optional)
            extra_css: New CSS styles (optional)

        Returns:
            Dictionary containing the updated template details

        Example:
            >>> template = client.templates.update(
            ...     template_id='template-c2465c0b-fc54-4672-b9ac-7446886cd6de',
            ...     name='Updated Template Name',
            ...     is_active=False
            ... )
        """
        data = {}
        if name is not None:
            data["name"] = name
        if content is not None:
            data["content"] = content
        if is_active is not None:
            data["is_active"] = is_active
        if extra_css is not None:
            data["extra_css"] = extra_css

        response = self._client.patch(f"templates/{template_id}", data=data)
        return response

    def delete(self, template_id: str) -> Dict[str, Any]:
        """
        Delete a template

        Args:
            template_id: The template ID to delete

        Returns:
            Dictionary containing the deletion result

        Example:
            >>> result = client.templates.delete('template-c2465c0b-fc54-4672-b9ac-7446886cd6de')
        """
        response = self._client.delete(f"templates/{template_id}")
        return response
