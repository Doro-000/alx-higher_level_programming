#!/usr/bin/python3

"""argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe version"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    command = """SELECT * FROM states
                 WHERE name = %s
                 ORDER BY states.id ASC"""
    cursor.execute(command, (argv[4].strip("'"),))
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.close()
