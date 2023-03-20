#!/usr/bin/python3
"""
define class city
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from relationship_state import State, Base


class City(Base):
    """
    class city instance Base
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
