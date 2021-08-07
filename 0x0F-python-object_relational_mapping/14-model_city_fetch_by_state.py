#!/usr/bin/python3

"""prints all City objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)

    my_session = session()

    for s, c in my_session.query(
        State, City).filter(
        State.id == City.state_id).order_by(
            City.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    my_session.close()
