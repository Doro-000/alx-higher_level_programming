#!/usr/bin/python3

"""creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa"""

from relationship_state import Base, State
from relationship_city import City 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)

    my_session = session()
    my_city = City(name="San Francisco")

    my_session.close()