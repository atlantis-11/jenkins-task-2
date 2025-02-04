from flask import Flask, jsonify, request

from .utils import format_weather_data, get_weather

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def weather():
    lat = request.args.get('lat', type=float)
    long = request.args.get('long', type=float)

    if lat is None or long is None:
        return jsonify({'error': 'Latitude and longitude are required'}), 400

    weather_data = get_weather(lat, long)
    formatted_data = format_weather_data(weather_data)

    return jsonify(formatted_data)
