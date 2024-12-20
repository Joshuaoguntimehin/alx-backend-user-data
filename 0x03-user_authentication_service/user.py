#!/usr/bin/env python3
"""
import statement
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for storing user credentials and session details.

    Attributes:
        id (int): Primary key, auto-incremented.
        email (str): User's  250 characters.
        hashed_password (strax length 250 characters.
        session_id (str): Seh 250 characters, nullable.
        reset_token (str): T50 characters, nullable.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
