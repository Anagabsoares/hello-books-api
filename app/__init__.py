from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# set the configurations for your application


def create_app():
    app = Flask(__name__)

    from .routes.py import books_bp
    app.register_blueprint(books_bp)

    return app