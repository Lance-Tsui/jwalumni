from models import mysql

# Define the User model
class News:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def find_news():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title, summary, content, publishdate, name FROM alu_news A JOIN alu_editor B on A.publishby = B.Id')
        rows = cur.fetchall()
        rows = list(rows)
        users = rows
        return users
