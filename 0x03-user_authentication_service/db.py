#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user
    
    def find_user_by(self, **kwargs) -> User:
        """
        Find a user based on provided query arguments (e.g., email, username).
        Raises InvalidRequestError if any invalid field is queried.
        Returns a User object if found.
        """
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError("Invalid query arguments provided")

        user = self.__session.query(User).filter_by(**kwargs).first()

        if user:
            return user
        raise NoResultFound("User not found")
