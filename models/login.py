from models import mysql
from hashlib import md5


# define the admin model
class Admin:
    @staticmethod
    def check_credentials(username, password):
        cur = mysql.connection.cursor()

        # Hash the provided password with MD5
        hashed_password = md5(password.encode()).hexdigest()

        # Query the database for the user with the provided username and hashed password
        cur.execute("SELECT * FROM alu_editor WHERE username = %s AND password = %s", (username, hashed_password))
        user = cur.fetchone()

        cur.close()

        return user
