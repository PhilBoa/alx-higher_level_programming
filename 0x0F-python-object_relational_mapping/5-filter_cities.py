#!/usr/bin/python3
"""
This script links to a MySQL database and retrieves all cities of
a given state as a command line argument.
"""


import MySQLdb
from sys import argv


def main():
    """
      Main function that connects to the MySQL database and retrieves cities
      of a state.
      """
    if len(argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state = argv[4]
    con = None
    cursor = None
    try:
        con = MySQLdb.connect(
                host="localhost",
                port=3306, user=user, password=password, db=db_name)
        cursor = con.cursor()
        query = "SELECT cities.id, cities.name " \
                "FROM cities " \
                "INNER JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC"
        cursor.execute(query, (state,))
        rows = cursor.fetchall()
        cities = [row[1] for row in rows]
        cities_str = ", ".join(cities)
        print(cities_str)
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL server: ", e)
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


if __name__ == "__main__":
    main()
