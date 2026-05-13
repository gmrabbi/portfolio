from app import db
from datetime import datetime


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    provider = db.Column(db.String(200), nullable=False)  # Organization providing training
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    certificate_url = db.Column(db.String(300))
    order = db.Column(db.Integer, default=0)  # For ordering display
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Training {self.title}>'
