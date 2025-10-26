from flask import Blueprint, request, render_template, redirect, url_for, session, flash, make_response

users_bp = Blueprint('users', __name__, template_folder='templates')

VALID_USER = {
    'username': 'student',
    'password': 'password123'
}

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if username == VALID_USER['username'] and password == VALID_USER['password']:
            session['user'] = username
            flash('Вхід успішний', 'success')
            return redirect(url_for('users.profile'))
        else:
            flash('Невірний логін або пароль', 'danger')
            return redirect(url_for('users.login'))
    return render_template('users/login.html')

@users_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Ви вийшли з системи', 'info')
    return redirect(url_for('users.login'))

def login_required(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Будь ласка, увійдіть у систему', 'warning')
            return redirect(url_for('users.login'))
        return func(*args, **kwargs)
    return wrapper

@users_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    message = None
    resp = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_cookie':
            key = request.form.get('cookie_key', '').strip()
            val = request.form.get('cookie_value', '').strip()
            max_age = request.form.get('cookie_max_age', '').strip()
            if key:
                resp = make_response(redirect(url_for('users.profile')))
                if max_age.isdigit():
                    resp.set_cookie(key, val, max_age=int(max_age))
                else:
                    resp.set_cookie(key, val)
                flash(f'Cookie "{key}" додано', 'success')
                return resp
            else:
                flash('Ключ cookie не може бути порожнім', 'danger')
        elif action == 'delete_cookie':
            key = request.form.get('cookie_key_delete', '').strip()
            if key:
                resp = make_response(redirect(url_for('users.profile')))
                resp.delete_cookie(key)
                flash(f'Cookie "{key}" видалено', 'info')
                return resp
            else:
                flash('Вкажіть ключ для видалення', 'danger')
        elif action == 'clear_all_cookies':
            resp = make_response(redirect(url_for('users.profile')))
            for ckey in request.cookies.keys():
                resp.delete_cookie(ckey)
            flash('Всі cookies видалено', 'info')
            return resp

    user = session.get('user')
    cookies = request.cookies  
    theme = request.cookies.get('theme', 'light')
    return render_template('users/profile.html', user=user, cookies=cookies, theme=theme)

@users_bp.route('/theme/<mode>')
@login_required
def theme(mode):
    resp = make_response(redirect(url_for('users.profile')))
    if mode in ('light', 'dark'):
        resp.set_cookie('theme', mode, max_age=60*60*24*30) 
        flash(f'Тема встановлена: {mode}', 'success')
    else:
        flash('Невірна тема', 'danger')
    return resp
