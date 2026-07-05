from flask import Flask
from config import Config
from app.routes.home import home_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(home_bp)

    return app