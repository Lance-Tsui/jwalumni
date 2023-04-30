from flask import render_template
from . import views_bp

# Define the about page route
@views_bp.route('/news')
def news():
    return render_template('news.html')
