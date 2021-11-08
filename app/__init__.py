from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# load_dotenv says get variable from .env and make them enviroment variable
#os gives us access to the environment variables
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv() #access the virtual environment 


def create_app(test_config=None):
    #test config is passing None here, however when testing we can set  it to tru to switch the  database 
    app = Flask(__name__)

    if test_config is None:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        # if we pass a test_config switch the database being used 
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import books_bp, authors_bp, genres_bp
    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(genres_bp)

    from app.models.book import Book
    
    return app
    # todo\
    


