from flask import Flask

from config import Config

from app.routes.home import home_bp
from app.routes.dashboard import dashboard_bp
from app.routes.experiments import experiments_bp
from app.routes.reports import reports_bp
from app.routes.auth import auth_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(experiments_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(auth_bp)

    return app