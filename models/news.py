from models import mysql

# Define the User model
class News:
    def __init__(self, title, summary, content, publishdate, name):
        self.title = title
        self.summary = summary
        self.content = content
        self.publishdate = publishdate
        self.name = name

    @staticmethod
    def find_news():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title, summary, content, publishdate, name FROM alu_news A JOIN alu_editor B on A.publishby = B.Id')
        rows = cur.fetchall()
        rows = list(rows)
        news = []
        for row in rows:
            new = News(row[0], row[1], row[2], row[3], row[4])
            news.append(new)
        return news
