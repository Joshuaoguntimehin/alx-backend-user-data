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
        # Ensure the session is properly initialized
        if self.__session is None:
            raise Exception("Database session not initialized")

        # Check for valid query keys
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError("Invalid query arguments provided")

        # Perform the query
        user = self.__session.query(User).filter_by(**kwargs).first()

        # Return the user if found, otherwise raise NoResultFound
        if user:
            return user
        raise NoResultFound("User not found")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user in the database based on user_id.
        :param user_id: ID of the user to be updated (int)
        :param kwargs: The attributes and values to update in the user record (dict)
        :return: None
        """
        user_to_update = self.find_user_by(id=user_id)
        for attr, value in kwargs.items():
            if hasattr(User, attr):
               setattr(user_to_update, attr, value)
            else:
                raise ValueError(f"Invalid attribute: {attr}")
        self._session.commit()
