from flask import render_template, request
from . import views_bp
from models.users import User

# Define the about page route
@views_bp.route('/explore')
def explore():
    query = request.args.get('q')
    users = User.find_all()
    result = []
    if query:
        for i in users:
            if query.lower() in i.title.lower():
                result.append(i)
        users = result

    return render_template('explore.html', users=users)
