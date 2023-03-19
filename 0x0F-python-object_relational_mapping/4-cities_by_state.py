#!/usr/bin/python3
import MySQLdb
"""
Lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=argv[1],
                         password=argv[2], db=argv[4])
    with db.cursor() as cur:
        cur.execute("""
                    SELECT cities.id, cities.name, state.name
                    From cities
                    JOIN states
                    ON cities.states_id = states.id
                    ORDER BY cities.id ASC
                    """)
        row = cur.fetchall()

    if row is not None:
        for row in rows:
            print(row)
