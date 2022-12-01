#!/usr/bin/python3
"""
creates a state class and base, an instance of declarative_base()
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first():
    for instance in result:
        print(f'{instance.id}: {instance.name}')
    if not result:
        print('Nothing')
        print()