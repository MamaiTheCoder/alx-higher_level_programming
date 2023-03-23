#!/usr/bin/python3
import MySQLdb
import sys
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == '__main__':
    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch data from the states table
    query = "SELECT * 
             FROM states 
             WHERE name LIKE BINARY '{}' 
             ORDER BY id ASC".format(sys.argv[4])

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Disconnect from the database
    db.close()
