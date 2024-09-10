
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    cover_photo = db.Column(db.String(255))
    number_of_pages = db.Column(db.Integer)
    description = db.Column(db.Text)
