#!/usr/bin/python3
import MySQLdb
import sys

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], port=3306)
cursor = db.cursor()

# Execute the query to select all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()

# Display the results
for state in states:
    print(state)

# Close the cursor and connection
cursor.close()
db.close()
