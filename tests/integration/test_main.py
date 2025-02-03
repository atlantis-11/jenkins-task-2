from unittest.mock import patch

from weather_app.utils import get_weather


def test_get_weather_success():
    mock_response = {
        'current': {
            'time': '2025-02-03T12:15',
            'temperature_2m': 4.1,
            'wind_speed_10m': 5.4,
        }
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = get_weather(52.52, 13.41)
        assert response == mock_response['current']
