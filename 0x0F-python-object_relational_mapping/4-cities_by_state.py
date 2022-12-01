#!/usr/bin/python3
'''
this is a print cities module
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)