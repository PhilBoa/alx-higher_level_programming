#!/usr/bin/python3
"""
Lists all State objects containing the letter a from the
database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and retrieves
    State objects containing the letter 'a'.
    """
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             user, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
                            State.name.like('%a%').order_by(State.id).all())
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
