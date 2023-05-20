from flask_mysqldb import MySQL

# Initialize the Flask app instance
mysql = MySQL()

# MySQL configurations
def connect_to_database(app): 
    app.config['MYSQL_HOST'] = '143.110.221.216'
    app.config['MYSQL_USER'] = 'schooluser'
    app.config['MYSQL_PASSWORD'] = 'jwalumni1926'
    app.config['MYSQL_DB'] = 'school'
    app.config['MYSQL_PORT'] = 3306
    mysql.init_app(app)

