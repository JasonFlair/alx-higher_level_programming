#!/usr/bin/python3
'''This is a module'''

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State('Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
