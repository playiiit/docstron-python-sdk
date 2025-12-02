"""
Usage resource for the Docstron API
"""

from typing import Dict, Any


class Usage:
    """Get usage statistics and limits"""

    def __init__(self, client):
        self._client = client

    def get(self) -> Dict[str, Any]:
        """
        Get usage statistics and limits

        Returns:
            Dictionary containing usage statistics for:
            - Applications (total, limit, usage_percentage)
            - Templates (total, limit, usage_percentage)
            - Documents (total, monthly, usage, monthly_limit, usage_percentage)
            - Subscription (plan_name, api_rate_limit, processing_priority, support_level)

        Example:
            >>> usage = client.usage.get()
            >>> print(f"Documents used: {usage['data']['documents']['monthly']}")
            >>> print(f"Monthly limit: {usage['data']['documents']['monthly_limit']}")
            >>> print(f"Plan: {usage['data']['subscription']['plan_name']}")
        """
        response = self._client.get("usage")
        return response
