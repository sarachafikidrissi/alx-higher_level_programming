#!/usr/bin/python3
"""This is model_city.py module
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """This is City  class that inherites from Base

    Attributes:
        id (INT) : calss attribute represents a column of unique integer
        name (str) : class attribute that represents a column of a string
        state_id (int) : class attribute represents a columnn of integer
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
