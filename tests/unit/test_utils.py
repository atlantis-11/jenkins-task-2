from weather_app.utils import format_weather_data


def test_format_weather_data():
    sample_data = {
        'time': '2025-02-03T12:15',
        'temperature_2m': 4.1,
        'wind_speed_10m': 5.4,
    }

    formatted = format_weather_data(sample_data)

    assert 'Temperature: 4.1°C' in formatted
    assert 'Wind Speed: 5.4 km/h' in formatted


def test_format_weather_data_no_data():
    assert format_weather_data(None) == 'No weather data available'
