from flask import Flask

from config import Config

from app.extensions import db
from app.extensions import migrate

from app.routes.home import home_bp
from app.routes.dashboard import dashboard_bp
from app.routes.experiments import experiments_bp
from app.routes.reports import reports_bp
from app.routes.auth import auth_bp
from app.models import User, Experiment

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(experiments_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(auth_bp)

    return app