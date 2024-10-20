import requests
from datetime import datetime

API_KEY = 'f3e0028da1e276c985ee9f5c8f03da19'  # Replace with your OpenWeatherMap API key

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None

def process_weather_data(data):
    if data:
        main = data['main']
        weather = data['weather'][0]
        city = data['name']
        timestamp = data['dt']

        processed_data = {
            'city': city,
            'temperature': main['temp'],  # Already in Celsius
            'feels_like': main['feels_like'],  # Already in Celsius
            'condition': weather['main'],
            'timestamp': datetime.fromtimestamp(timestamp)
        }
        return processed_data
    return None