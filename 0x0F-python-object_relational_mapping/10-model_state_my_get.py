#!/usr/bin/python3
"""start habing conversation with database
"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    if (len(args) != 5):
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data))
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    state_id = session.query(State).filter(State.name == state_name)\
                      .order_by(State.id)

    if state_id is not None and state_id.count() > 0:
        for _id in state_id:
            print(_id.id)
    else:
        print("Not found")
