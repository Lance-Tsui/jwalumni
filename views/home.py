from flask import render_template
from . import views_bp

# Define the home page route
@views_bp.route('/')
def home():
    return render_template('home.html')
