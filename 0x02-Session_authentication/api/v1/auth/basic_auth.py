#!/usr/bin/env python3
"""Basic authentication module"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User

class BasicAuth(Auth):
    """BasicAuth class for implementing Basic Authentication."""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The full Authorization header.

        Returns:
            str: The Base64 encoded string or None if invalid.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 encoded Authorization header.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str: The decoded string or None if decoding fails.
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract user email and password from a decoded Base64 Authorization header.

        Args:
            decoded_base64_authorization_header (str): Decoded Base64 string.

        Returns:
            tuple: (email, password) if valid, otherwise (None, None).
        """
        if not isinstance(decoded_base64_authorization_header, str) or ':' not in decoded_base64_authorization_header:
            return None, None

        """ Split on the first occurrence of ':' to separate email and password"""
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    from typing import TypeVar

class BasicAuth:
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieve the User instance based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            TypeVar('User'): The User instance if credentials are valid, otherwise None.
        """
        # Validate email input
        if user_email is None or not isinstance(user_email, str):
            return None

        # Validate password input
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for user by email
        from models.user import User  # Import User class if not already done
        users = User.search({'email': user_email})
        
        if not users or len(users) == 0:
            return None

        user = users[0]  # Assume email is unique, so one result
        if not user.is_valid_password(user_pwd):
            return None

        return user
