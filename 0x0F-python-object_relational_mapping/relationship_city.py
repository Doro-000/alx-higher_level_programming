#!/usr/bin/python3

""" contains the class definition of a city"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base, State


class City(Base):
    """class representing city Table"""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
