"""
Applications resource for the Docstron API
"""

from typing import Dict, Any, List


class Applications:
    """Manage Docstron applications"""

    def __init__(self, client):
        self._client = client

    def get(self, app_id: str) -> Dict[str, Any]:
        """
        Get a specific application by ID

        Args:
            app_id: The application ID (e.g., 'app-7b4d78fb-820c-4ca9-84cc-46953f211234')

        Returns:
            Dictionary containing application details

        Example:
            >>> app = client.applications.get('app-7b4d78fb-820c-4ca9-84cc-46953f211234')
            >>> print(app['data']['name'])
        """
        response = self._client.get(f"applications/{app_id}")
        return response

    def list(self) -> List[Dict[str, Any]]:
        """
        Get all applications

        Returns:
            List of dictionaries containing application details

        Example:
            >>> apps = client.applications.list()
            >>> for app in apps['data']:
            ...     print(app['name'])
        """
        response = self._client.get("applications")
        return response
