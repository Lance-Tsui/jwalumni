from flask import Flask, send_from_directory
from models import connect_to_database
from views import views_bp

# Initialize the Flask app
app = Flask(__name__)

# Connect to the database
connect_to_database(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'static/img/favicon.ico', mimetype='image/vnd.microsoft.icon')

app.register_blueprint(views_bp)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
