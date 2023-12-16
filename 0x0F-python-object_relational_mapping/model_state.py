#!/usr/bin/python3
"""This is model_state.py module
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()


class State(Base):
    """This is states class that inherites from Base

    Attributes:
        id (INT) : calss attribute represents a column of unique integer
        name (str) : class attribute that represents a column of a string
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
