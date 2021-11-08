from app import db 

class Genre(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String())
