#!/usr/bin/python3

"""
create state "California" with city attribute "San Francisco"
parameters given to script: username, password, database
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    # make engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_c = City(name="California")
    new_s = State(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_c)
    session.add(new_s)

    session.commit()
    session.close()
