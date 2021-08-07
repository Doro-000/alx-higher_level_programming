#!/usr/bin/python3

"""lists all City objects from the database hbtn_0e_101_usa"""

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

    for city in my_session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    my_session.close()
