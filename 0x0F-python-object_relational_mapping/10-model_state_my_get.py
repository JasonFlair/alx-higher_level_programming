#!/usr/bin/python3
"""
a module that rows(states) with a in them
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(State.name.like(sys.argv[4]))
    for result in results:
        if result is None:
            print("Nothing found")
        else:
            print(f'{result.id}')

    session.close()
