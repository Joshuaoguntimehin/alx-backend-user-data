#!/usr/bin/env python3
"""import stetement"""
from flask import request
from typing import List, TypeVar
User = TypeVar('User')

class Auth():
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        return False
    
    def authorization_header(self, request=None) -> str:
        return None
    
    def current_user(self, request=None) -> User:
        return None