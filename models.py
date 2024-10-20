# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    avg_temp = db.Column(db.Float)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    dominant_condition = db.Column(db.String(50))

    def __repr__(self):
        return f"<WeatherSummary {self.city} on {self.date}>"