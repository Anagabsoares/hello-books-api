'''#!  A standard pytest file that holds test configurations 
#!     and common test helper functions. Essentially, 
#!    this file is run before any other test files. This allows fixtures registered here to be available to any other test file.
'''
import pytest
from app import create_app
from app.models.book import Book
from app import db

@pytest.fixture
# name it whatver resource we want to access
def app():
    app = create_app({"TESTING": True})
    # instance of app, and set configuration to True
    with app.app_context():
        # in the context of the app we just created
        db.create_all()
        # creating all the tables and that is why we dont need to use migration for this specific case here
        # it is already handling the creatin for us
        # creates a new database -

        yield app
        # stops app and run tests after is done execute next lines 

    with app.app_context():
        db.drop_all()
        # for each test we want a fresh SQLALCHEMY_DATABASE_URI
        # cleans 


@pytest.fixture
def client(app):
    # this fixture depend on an intance of the app fixture 
    # injects in  app  before it cleans the database 
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                    description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                    description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()