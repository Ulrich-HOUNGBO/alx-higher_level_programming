#!/usr/bin/python3
"""
return all table values (table 'states') that statting with N
parameters given to script: username, password, database
"""
import MYSQLdb
from sys import argv

if __name__ == '__main__':
    #connect to database
    db=MYSQLdb.connect(host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3])
    # create cursor to exec queries using SQL; filter names starting with 'N'
    cur= db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0]='N':
            print(row)
    cur.close() 
    db.close()

