from flask import Flask, render_template
from .config import DevelopmentConfig
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import main_bp
    from .users.views import users_bp
    from .products.views import products_bp
    from .posts.views import posts_bp   

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(posts_bp, url_prefix='/post')   

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app