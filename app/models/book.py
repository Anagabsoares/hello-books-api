from sqlalchemy.orm import backref
from app import db 

class Book(db.Model):
    #! The class book inherits from db.Model from SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    #! one-to-many relationship
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")
    #! many-to-many genres
    genres= db.relationship("Genre", backref="books", secondary="books_genres")


