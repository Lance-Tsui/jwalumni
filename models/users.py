from models import mysql

# Define the User model
class User:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def find_all():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title FROM alu_info')
        row = cur.fetchone()
        cur.close()
        if row is None:
            return None
        return User(*row)
