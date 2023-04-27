from flask import render_template
from . import views_bp
from models.users import User

# Define the about page route
@views_bp.route('/about')
def about():
    users = User.find_all()
    return render_template('about.html', users=users)
