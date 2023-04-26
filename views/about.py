from flask import render_template
from . import views_bp

# Define the about page route
@views_bp.route('/about')
def about():
    return render_template('about.html')
