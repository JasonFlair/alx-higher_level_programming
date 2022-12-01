#!/usr/bin/python3
'''
this is a print cities module
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.name FROM cities WHERE cities.state_id = (SELECT id FROM states WHERE states.name = %s)", (sys.argv[4], ))
    rows = mycursor.fetchall()
    for row in rows:
        print(row[i])
    mycursor.close()
    db.close()