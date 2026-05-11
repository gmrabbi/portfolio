from app import db
from datetime import datetime


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    journal = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.String(500))
    link = db.Column(db.String(500))
    status = db.Column(db.String(100), default='Published')  # Published, In Review, etc.
    publication_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Publication {self.title}>'
