#!/usr/bin/python3
"""This is a module for updating a name"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    the_state = session.query(State).filter(State.id == 2).first()
    the_state.name = 'New Mexico'
    session.commit()
    session.close()
