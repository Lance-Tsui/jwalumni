from models import mysql

# Define the User model
class User:
    def __init__(self, title, region):
        self.title = title
        self.region = region

    @staticmethod
    def find_all():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title, region FROM alu_info A JOIN alu_region B on A.regionId = B.Id')
        rows = cur.fetchall()
        rows = list(rows)
        users = rows
        return users
