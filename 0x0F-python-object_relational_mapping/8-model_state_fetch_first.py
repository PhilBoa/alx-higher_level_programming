#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and retrieves
    the first State object.
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
    first_state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(first_state.id, first_state.name))
    session.close()


if __name__ == "__main__":
    main()
