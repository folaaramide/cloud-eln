from flask import Blueprint, render_template

experiments_bp = Blueprint("experiments", __name__)


@experiments_bp.route("/experiments")
def experiments():
    return render_template("experiments.html")