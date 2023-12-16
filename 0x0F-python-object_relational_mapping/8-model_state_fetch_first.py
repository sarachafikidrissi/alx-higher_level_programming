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
    if (len(args) != 4):
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data))
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    state_name = session.query(State).order_by(State.id).first()

    if state_name is not None:
        print('{}: {}'.format(state_name.id, state_name.name))
    else:
        print('Nothing')
