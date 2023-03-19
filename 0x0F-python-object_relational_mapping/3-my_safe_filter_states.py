#!/usr/bin/python3
"""
return matching states; safe from MySQL injections
# http://bobby-tables.com/python
parameters given to script: username, password, database, state to match
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
    sql_cmd = """SELECT * FROM states WHERE name=%s ORDER BY id ASC"""
    cur.execute(sql_cmd, (argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
