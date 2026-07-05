from app.auth.forms import LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash

from app.auth.forms import RegistrationForm
from app.extensions import db, bcrypt
from app.models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            password=hashed_password,
            role=form.role.data
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!", "success")

        return redirect(url_for("auth.login"))

    return render_template(
        "register.html",
        form=form
    )

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    return render_template(
        "login.html",
        form=form
    )