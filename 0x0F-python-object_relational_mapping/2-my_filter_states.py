#!/usr/bin/python3
"""
This is a filter module.
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states WHERE states.name LIKE BINARY '{}' ORDER BY id".format(sys.argv[4]))
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
