from app import db
from datetime import datetime


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(200), nullable=False)
    degree = db.Column(db.String(100), nullable=False)  # B.Sc., Diploma, SSC, etc.
    field_of_study = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    cgpa = db.Column(db.Float)  # CGPA or GPA
    cgpa_scale = db.Column(db.String(20), default='4.00')  # e.g., 4.00, 5.00
    description = db.Column(db.Text)
    current = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)  # For ordering display
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Education {self.degree} - {self.institution}>'
