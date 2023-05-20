from flask import render_template
from . import views_bp
from models.news import News

# Define the article page route

@views_bp.route('/news/<new_title>')
def news_content(new_title):
    article = News.find_news_content(new_title)
    return render_template('article.html', article=article)
