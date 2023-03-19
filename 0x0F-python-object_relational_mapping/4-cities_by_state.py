#!/usr/bin/python3
"""
return info from both tables (tables 'cities' 'states)
parameters given to script: username, password, database
"""

from sys import argv

import MySQLdb

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; join two tables for all info
    cur = db.cursor()
    sql_cmd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cur.execute(sql_cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
