import requests

_api_url = 'https://api.open-meteo.com/v1/forecast'


def get_weather(lat, long):
    response = requests.get(
        f'{_api_url}?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m'
    )

    if response.status_code == 200:
        return response.json()['current']
    else:
        return None


def format_weather_data(weather_data):
    if not weather_data:
        return 'No weather data available'

    return (
        f"Temperature: {weather_data.get('temperature_2m', 'N/A')}°C\n"
        f"Wind Speed: {weather_data.get('wind_speed_10m', 'N/A')} km/h"
    )
