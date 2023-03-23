#!/usr/bin/python3
import MySQLdb
import sys
"""
Lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username, password, database = sys.argv[1:]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306)

        cur = db.cursor()
        cur.execute("SELECT * FROM cities ORDER BY id ASC")

        for row in cur.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        exit(1)

    finally:
        db.close()
