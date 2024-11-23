#!/usr/bin/env python3
"""
Import statements
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash the password using bcrypt and return the hashed password.
    
    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the email and password."""
        try:
            # Check if user already exists
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            # User does not exist, continue with registration
            pass
        
        # Hash the password
        hashed_password = _hash_password(password)
        
        # Add the new user to the database
        new_user = self._db.add_user(email=email,
                                     hashed_password=hashed_password.decode("utf-8"))
        
        # Return the new user object
        return new_user