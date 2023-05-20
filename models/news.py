from models import mysql


# Define the News model
class News:
    def __init__(self, title, summary=None, content=None, publishdate=None, publishby=None):
        self.title = title
        self.summary = summary
        self.content = content
        self.publishdate = publishdate
        self.publishby = publishby

    @staticmethod
    def find_news():
        cur = mysql.connection.cursor()
        cur.execute('SELECT title FROM alu_news A JOIN alu_editor B on A.publishby = B.Id')
        rows = cur.fetchall()
        rows = list(rows)
        news = []
        for row in rows:
            new = News(row[0])
            news.append(new)
        return news

    @staticmethod
    def find_news_content(title):
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT title, summary, content, publishdate, username FROM alu_news A JOIN alu_editor B on A.publishby = B.Id where title = "' + title + '"')
        row = cur.fetchone()
        new = News(row[0], row[1], row[2], row[3], row[4])
        return new
