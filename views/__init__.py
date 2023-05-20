from flask import Blueprint

# Create a Blueprint object for the views
views_bp = Blueprint('views', __name__)

# Import the views
from .home import *
from .news import *
from .explore import *
from .article import *
from .login import *
