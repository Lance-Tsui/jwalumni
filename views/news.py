from flask import render_template
from . import views_bp
from models.news import News

# Define the about page route
@views_bp.route('/news')
def news():
    news = News.find_news()
    return render_template('news.html', news=news)
