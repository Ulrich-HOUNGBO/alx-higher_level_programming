#!/usr/bin/python3
"""
list all state objects from database that contain the letter a
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
    for instance in session.query(State).filter(State.name.like('%a%')). \
            order_by(State.id).frist():
        print("{:d}: {:s}".format(instance.id, instance.name))
    session.close()
