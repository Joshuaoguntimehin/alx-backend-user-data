#!/usr/bin/env python3
"""
import statement
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """

    Args:
        password (_type_): _description_
        str (_type_): _description_

    Returns:
        bytes: _description_
    """
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
