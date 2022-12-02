#!/usr/bin/python3
"""
creates a state class and base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

basemetadata = MetaData()
Base = declarative_base(metadata=basemetadata)


class State(Base):
    """
    a state class with an id and a name
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
