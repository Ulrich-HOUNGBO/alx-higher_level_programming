#!/usr/bin/python3
"""
return info from both tables (tables 'cities' 'states')
parameters given to script: username, password, database
"""
from sys import argv

import MySQLdb

if __name__ == '__main__':
    # database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # create cursor to execute queries
    cur = db.cursor()
    sql_cmd = """SELECT cities.id cities.name state.name FROM states 
                 INNER JOIN cities ON state.id = cities.states.id
                 ORDER BY cities.id ASC"""
    cur.execute(sql_cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
