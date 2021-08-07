#!/usr/bin/python3

"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    my_session = Session()
    new_state = State(name="Louisiana")
    my_session.add(new_state)
    my_session.commit()
    print(new_state.id)
    my_session.close()
