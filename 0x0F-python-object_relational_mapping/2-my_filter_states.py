#!/usr/bin/python3

"""This module is for listing states from
a Database
"""


import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database = args[3]
    user_input = args[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()

    num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                           '{}'".format(user_input))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
