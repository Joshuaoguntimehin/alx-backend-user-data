#!/usr/bin/env python3
"""Basic authentication module"""

from api.v1.auth.auth import Auth
import base64

class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header."""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            """Decode the Base64 encoded string"""
            decoded_bytes = base64.b64decode(base64_authorization_header)
            """Convert bytes to UTF-8 string"""
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            """Return None if decoding fails"""
            return None
