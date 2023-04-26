from flask import Blueprint

# Create a Blueprint object for the views
views_bp = Blueprint('views', __name__)

# Import the views
from .home import *
from .about import *

# Register the views with the Flask app
def register_views(app):
    app.register_blueprint(views_bp)
