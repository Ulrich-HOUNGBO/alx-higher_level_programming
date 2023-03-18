#!/usr/bin/python3
"""
return matching states
parameters given to script: username, password, database, state to match
"""
import MySQL
from sys import argv
if __name == '__main__':
    #connect to database
    db = MySQL.connect(host="localhost",
                        port = 3306,
                        user = argv[1],
                        passwd = argv[2],
                        db = argv[3])
    #create cursor to execute queries
    cur = db.cursor()
    sql_cmd = """SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY is ASC""".format(argv[4])
    cur.execute(sql_cmd)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()

