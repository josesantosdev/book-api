from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db
from .serealize import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    
    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db)
    
    
    from .autor import bp_autor
    from .book import bp_book
    
    app.register_blueprint(bp_autor, url_prefix='/api/v1')
    app.register_blueprint(bp_book, url_prefix='/api/v1')
    
    return app