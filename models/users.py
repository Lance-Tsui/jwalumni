from models import mysql

# Define the User model
class User:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def find_all():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title FROM alu_info')
        rows = cur.fetchall()
        rows = list(rows)
        users = []
        for row in rows:
            row = list(row)
            user = User(row)
            users.append(user)
        cur.close()
        return users
