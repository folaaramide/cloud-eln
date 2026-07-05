import os


class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///eln.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False