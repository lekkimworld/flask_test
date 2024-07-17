import os

from flask import Flask
from dotenv import load_dotenv
from .views.home_bp import home_bp
from .views.json_bp import json_bp


def create_app(test_config=None):
    """Factory to create the Flask application
    :return: A `Flask` application instance
    """
    app = Flask(__name__)
    load_dotenv()
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if test_config:
        app.config.update(test_config)
    _register_blueprints(app)
    return app


def _register_blueprints(app):
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(json_bp, url_prefix="/api")
