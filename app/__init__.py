from flask import Flask
from instance.config import app_config
from resources.books import books_api
from resources.users import user_api
from resources.doc import doc_api
from app.models import db


def create_app(config_name):
    """Create flask app"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    # Enable swagger editor
    app.config['SWAGGER_UI_JSONEDITOR'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    # Register blueprints to application
    app.register_blueprint(books_api, url_prefix='/api/v2')
    app.register_blueprint(user_api, url_prefix='/api/v2')
    app.register_blueprint(doc_api, url_prefix='/api/v2')

    return app
