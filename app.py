from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from threading import Thread
import time
from weather import get_weather_data, process_weather_data
from models import db, WeatherSummary
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather_data():
    while True:
        for city in cities:
            data = get_weather_data(city)
            processed_data = process_weather_data(data)
            # Store processed data in DB, calculate summaries, etc.
            print(processed_data)  # For demonstration
        time.sleep(Config.FETCH_INTERVAL)

def init():
    with app.app_context():  # Ensure the app context is available
        db.create_all()  # Create database tables
    Thread(target=fetch_weather_data).start()  # Start the data fetching thread

if __name__ == '__main__':
    init()  # Initialize the app and database
    app.run(debug=True)  # Run the application