#!/usr/bin/python3

"""prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    my_session = Session()

    try:
        row = my_session.query(State.id, State.name).order_by(State.id)[0]
        print("{}: {}".format(row.id, row.name))
    except BaseException:
        print("Nothing")
    my_session.close()
