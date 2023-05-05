from flask import Flask, Blueprint, render_template
from models import mysql, connect_to_database
from models.users import User
from models.news import News
from views import views_bp

# Initialize the Flask app
app = Flask(__name__)

# Connect to the database
connect_to_database(app)

app.register_blueprint(views_bp)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
