#!/usr/bin/python3

"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    command = """SELECT * FROM states
                 WHERE name REGEXP '^N'
                 ORDER BY states.id ASC"""
    cursor.execute(command)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.close()
