from flask import render_template, request, jsonify
from . import views_bp
from models.users import User

# Define the about page route
@views_bp.route('/explore')
def explore():
    users = User.find_all()
    return render_template('explore.html', users=users)

@views_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    drop = request.args.get('d')
    users = User.find_all()
    if query:
        result = []
        for i in users:
            if query.lower() in i.title.lower():
                result.append(i)
        users = result

    if drop:
        result = []
        for i in users:
            if i.region.lower() == drop.lower():
                result.append(i)
        users = result

    # 只返回用户列表的 JSON 数据，不返回整个 HTML 页面
    return jsonify(users=[{'title': user.title, 'region': user.region} for user in users])
