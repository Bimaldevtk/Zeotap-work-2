# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'  # SQLite database for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FETCH_INTERVAL = 300  # Fetch data every 5 minutes
