from flask import Flask, render_template
from models import mysql, connect_to_database

# Initialize the Flask app
app = Flask(__name__)

# Connect to the database
connect_to_database(app)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the about page route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
