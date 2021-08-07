#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    command = """SELECT cities.id, cities.name, states.name
                 FROM cities
                 JOIN states
                 ON cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    cursor.execute(command)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.close()
