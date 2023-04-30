from flask import render_template
from . import views_bp
from models.users import User

# Define the about page route
@views_bp.route('/explore')
def explore():
    users = User.find_all()
    return render_template('explore.html', users=users)
