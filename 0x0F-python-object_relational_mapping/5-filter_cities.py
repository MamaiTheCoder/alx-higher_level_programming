#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Check if 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)
    
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)

    # Create cursor
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT cities.id, cities.name, states.name 
                    FROM cities 
                    JOIN states ON cities.state_id = states.id 
                    WHERE states.name LIKE %s 
                    ORDER BY cities.id ASC", (state_name,))

    # Get results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print("{}: ({}) {}".format(row[2], row[0], row[1]))

    # Close cursor and database connection
    cursor.close()
    db.close()

    
    
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name
                FROM cities 
                JOIN states 
                ON cities.state_id = states.id
                WHERE states.name = '{}';".format(sys.argv[4]))
    states = cur.fetchall()

    print(", ".join([state[1] for state in states]))
                
                
