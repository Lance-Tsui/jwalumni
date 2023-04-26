from models import mysql

# Define the User model
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @staticmethod
    def find_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id = %s', (id,))
        row = cur.fetchone()
        cur.close()

        if row is None:
            return None

        return User(*row)
