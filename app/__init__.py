from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')

# імпортуємо і реєструємо маршрути/blueprints
from .views import main_bp
app.register_blueprint(main_bp)

# users blueprint (url prefix /users)
from .users.views import users_bp
app.register_blueprint(users_bp, url_prefix='/users')

# products blueprint (url prefix /products)
from .products.views import products_bp
app.register_blueprint(products_bp, url_prefix='/products')
