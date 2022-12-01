#!/usr/bin/python3
'''
this is a print cities module
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("select cities.name, states.name from cities inner join states on cities.state_id = states.id")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)