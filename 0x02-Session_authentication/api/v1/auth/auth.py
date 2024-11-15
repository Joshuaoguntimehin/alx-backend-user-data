#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication
        """
        if path is None or excluded_paths is None:
            return True 

        if not path.endswith('/'):
            path += '/'


        return path not in excluded_paths

        

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
