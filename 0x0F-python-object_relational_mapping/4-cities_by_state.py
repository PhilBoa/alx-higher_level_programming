#!/usr/bin/python3
"""
This script links to a MySQL database and retrieves all cities from the
'cities' table.
"""


import MySQLdb
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and retrieves all cities.
    """
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    con = None
    cursor = None
    try:
        con = MySQLdb.connect(
                host="localhost",
                port=3306, user=user, password=password, db=db_name)
        cursor = con.cursor()
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities " \
                "INNER JOIN states ON cities.state_id = states.id " \
                "ORDER BY cities.id ASC"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL server: ", e)
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


if __name__ == "__main__":
    main()
