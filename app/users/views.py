from flask import Blueprint, request, render_template, redirect, url_for

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/hi/<name>')
def greetings(name):
    age = request.args.get('age', '')
    return render_template('users/hi.html', name=name.upper(), age=age)

@users_bp.route('/admin')
def admin():
    return redirect(url_for('users.greetings', name='Administrator', age=45))
