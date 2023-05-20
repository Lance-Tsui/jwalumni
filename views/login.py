from flask import render_template, request, redirect

from . import views_bp

from models.login import Admin


@views_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        admin = Admin.check_credentials(username, password)

        if admin:
            # Login successful
            return redirect('/')
        else:
            # Invalid credentials
            return 'Invalid username or password'
    else:
        # Render the login template for 'GET' requests
        return render_template('login.html')
