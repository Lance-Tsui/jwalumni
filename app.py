from flask import Flask, render_template
from models import mysql, connect_to_database
from models.users import User
from models.news import News

# Initialize the Flask app
app = Flask(__name__)

# Connect to the database
connect_to_database(app)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the about page route
@app.route('/explore')
def explore():
    users = User.find_all()
    return render_template('explore.html', users=users)

# Define the news page route
@app.route('/news')
def news():
    news = News.find_news()
    return render_template('news.html', news=news)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
