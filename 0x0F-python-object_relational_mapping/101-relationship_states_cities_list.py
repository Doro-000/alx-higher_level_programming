#!/usr/bin/python3

"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    my_session = Session()

    for state in my_session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    my_session.close()
