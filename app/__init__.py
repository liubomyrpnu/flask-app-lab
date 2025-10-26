from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'dev-secret-for-lab4'

from .views import main_bp
app.register_blueprint(main_bp)

from .users.views import users_bp
app.register_blueprint(users_bp, url_prefix='/users')

from .products.views import products_bp
app.register_blueprint(products_bp, url_prefix='/products')
