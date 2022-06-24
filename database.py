import sqlite3

# Create a database or connect to an existing one


class Database():

    _conn = sqlite3.connect('homeworkhelp.db')

    # Create cursor
    global _c
    _c = _conn.cursor()

    # Create table
    _c.execute("""
               CREATE TABLE 
               users(username TEXT, 
               pass TEXT, 
               grade INT, 
               period1 TEXT, 
               period2 TEXT, 
               period3 TEXT, 
               period4 TEXT, 
               period5 TEXT, 
               period6 TEXT, 
               period7 TEXT, 
               period8 TEXT
               )
               """)

    # Functions for adding and reading the database

    def addNewUser(username: str, password: str, grade: str):
        _c.execute("INSERT INTO users VALUES (:username, :pass, :grade)",
                   {
                       'username': username,
                       'pass': password,
                       'grade': grade
                   })

    # Commit changes
    _conn.commit()

    # Close Connection
    _conn.close()
