#!/usr/bin/python3
"""
a module that retrieves all the rows
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City).all()
    for states, cities in result:
        print(f'{states.name}: {cities.id} {cities.name}')

    session.close()
