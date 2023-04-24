from flask import Flask
from flask_mysqldb import MySQL

# Initialize the Flask app instance
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '143.110.221.216'
app.config['MYSQL_USER'] = 'schooluser'
app.config['MYSQL_PASSWORD'] = 'jwalumni1926'
app.config['MYSQL_DB'] = 'school'

# Initialize the MySQL connection
mysql = MySQL(app)

# Import the views module and register the blueprint
from app import views
app.register_blueprint(views.bp)
