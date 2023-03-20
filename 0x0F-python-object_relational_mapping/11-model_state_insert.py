#!/usr/bin/python3
"""
update state: given id, change state name
parameters given to script: username, password, database
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # add new state and commit all
    new = State(name='Louisiana')
    session.add(new)
    session.commit()

    print("{:d}".format(new.id))
    session.close()
