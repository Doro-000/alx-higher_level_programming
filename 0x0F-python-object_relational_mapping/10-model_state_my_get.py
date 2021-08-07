#!/usr/bin/python3

"""prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

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
        row = my_session.query(State).filter(State.name == argv[4])[0]
        print(row.id)
    except BaseException:
        print("Not found")
    my_session.close()
