#!/usr/bin/python3
"""
return state id given state name; SQL injection free
parameters given to script: username, password, database, state name to match
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

    if instance := session.query(State).filter_by(name=argv[4]).first():
        print("{:d}".format(instance.id))
    else:
        print('Not found')
    session.close()
