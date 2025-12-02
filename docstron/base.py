"""
Base HTTP client for the Docstron API
"""

import requests
from typing import Dict, Any, Optional
from .exceptions import (
    DocstronError,
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError,
)


class BaseClient:
    """Base HTTP client with error handling"""

    def __init__(self, api_key: str, base_url: str = "https://api.docstron.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise appropriate exceptions"""
        try:
            data = response.json()
        except ValueError:
            data = {}

        if response.status_code == 200:
            return data
        elif response.status_code == 401:
            raise AuthenticationError(
                data.get("message", "Authentication failed"),
                status_code=response.status_code,
                response=data,
            )
        elif response.status_code == 404:
            raise NotFoundError(
                data.get("message", "Resource not found"),
                status_code=response.status_code,
                response=data,
            )
        elif response.status_code == 422:
            raise ValidationError(
                data.get("message", "Validation error"),
                status_code=response.status_code,
                response=data,
            )
        elif response.status_code == 429:
            raise RateLimitError(
                data.get("message", "Rate limit exceeded"),
                status_code=response.status_code,
                response=data,
            )
        elif response.status_code >= 500:
            raise ServerError(
                data.get("message", "Server error"),
                status_code=response.status_code,
                response=data,
            )
        else:
            raise DocstronError(
                data.get("message", "An error occurred"),
                status_code=response.status_code,
                response=data,
            )

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a GET request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        return self._handle_response(response)

    def post(
        self, endpoint: str, data: Optional[Dict] = None, files: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Make a POST request"""
        url = f"{self.base_url}/{endpoint}"
        if files:
            # Remove Content-Type header for multipart/form-data
            headers = self.session.headers.copy()
            headers.pop("Content-Type", None)
            response = self.session.post(url, data=data, files=files, headers=headers)
        else:
            response = self.session.post(url, json=data)
        return self._handle_response(response)

    def patch(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a PATCH request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.patch(url, json=data)
        return self._handle_response(response)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url)
        return self._handle_response(response)

    def post_binary(self, endpoint: str, data: Optional[Dict] = None) -> bytes:
        """Make a POST request that returns binary data (e.g., PDF)"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        if response.status_code == 200:
            return response.content
        else:
            return self._handle_response(response)

    def download(self, endpoint: str) -> bytes:
        """Download a file (returns binary data)"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return self._handle_response(response)
