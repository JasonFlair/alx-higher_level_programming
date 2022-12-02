#!/usr/bin/python3
"""
creates a state class and base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

basemetadata = MetaData()
Base = declarative_base(metadata=basemetadata)


class City(Base):
    """
    a cities class with an id and a name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id