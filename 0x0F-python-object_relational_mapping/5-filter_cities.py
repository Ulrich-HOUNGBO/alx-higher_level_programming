#!/usr/bin/python3
"""
return all cities from state given in argument
parameters given to script: username, password, database, state
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
    sql_cmd = """SELECT cities.name FROM cities 
                 INNER JOIN cities ON state.id = cities.state_id
                 WHERE states.name LIKE %s 
                 ORDER BY cities.id ASC"""
    cur.execute(sql_cmd)
    rows = cur.fetchall()
    # format the printing of cities of same state separated by commas
    for row in rows:
        print(', '.join(["{:s}".format(row[0])]))
    cur.close()
    db.close()
