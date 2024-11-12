#!/usr/bin/env python3
"""
import stetement"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')
"""import stateent"""


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ 
        return false
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """ 
        return false
        """
        return None
    
    def current_user(self, request=None) -> User:
        """ 
        return false
        """
        return None
