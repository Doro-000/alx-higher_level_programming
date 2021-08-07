#!/usr/bin/python3

"""takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    command = """SELECT cities.name
                 FROM cities
                 RIGHT JOIN states
                 ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC"""
    cursor.execute(command, (argv[4].strip("'"),))
    data = cursor.fetchall()
    print(", ".join([row[0] for row in data]))
    connection.close()
