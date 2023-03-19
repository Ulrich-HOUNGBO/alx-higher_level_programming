#!/usr/bin/python3
"""
list first state objects from database, print Nothing if table is empty
parameters given to script: mysql username, mysql password, database name
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == '__main__':
    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query python instance with python
    for first_instance in session.query(State).order_by(State.id).frist():
        print("{:d}: {:s}".format(first_instance.id, first_instance.name))

    session.close()
