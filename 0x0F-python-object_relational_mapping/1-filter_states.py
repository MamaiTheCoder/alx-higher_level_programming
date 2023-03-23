#!/usr/bin/python3
"""
Lists all states from database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object
    cur = conn.cursor()
    
    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all the results and store in a variable
    results = cur.fetchall()
    
    # Print the results in the desired format
    for row in results:
        if row[1][0] == 'N':
            print(row)
    
    # Close the cursor and connection
    cur.close()
    conn.close()
