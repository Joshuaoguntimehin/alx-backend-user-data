#!/usr/bin/env python3
"""
This module provides the `Auth` class for handling basic authentication in a Flask web application.

The `Auth` class includes methods for determining authentication requirements, retrieving
authorization headers, and identifying the current user.
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication management class for handling access control."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        excluded_paths = [p if p.endswith('/') else p + '/' for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request (Flask.request): The current request object.

        Returns:
            str: The Authorization header value, or None if not present.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current authenticated user.

        Args:
            request (Flask.request): The current request object.

        Returns:
            User: The current user object, or None if not available.
        """
        return None
