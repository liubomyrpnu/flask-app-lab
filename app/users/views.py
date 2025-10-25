from flask import Blueprint, request, render_template, redirect, url_for

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/hi/<name>')
def greetings(name):
    age = request.args.get('age', '')
    # передамо у шаблон; в шаблоні відобразимо ім'я великими літерами
    return render_template('users/hi.html', name=name.upper(), age=age)

@users_bp.route('/admin')
def admin():
    # при зверненні перенаправити на привітання адміністратора з віком 45
    return redirect(url_for('users.greetings', name='Administrator', age=45))
