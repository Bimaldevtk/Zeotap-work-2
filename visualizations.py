# visualizations.py
import matplotlib.pyplot as plt
import pandas as pd
from models import WeatherSummary

def plot_daily_summary():
    summaries = WeatherSummary.query.all()
    data = {
        "Date": [summary.date for summary in summaries],
        "Avg Temp": [summary.avg_temp for summary in summaries],
        "Max Temp": [summary.max_temp for summary in summaries],
        "Min Temp": [summary.min_temp for summary in summaries],
        "Dominant Condition": [summary.dominant_condition for summary in summaries]
    }
    df = pd.DataFrame(data)

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Avg Temp'], marker='o', label='Avg Temperature')
    plt.fill_between(df['Date'], df['Max Temp'], df['Min Temp'], color='gray', alpha=0.5, label='Temp Range')
    plt.title('Daily Weather Summary')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
