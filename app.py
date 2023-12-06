from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/weather')
def get_weather():
    location = request.args.get('location')
    weather_data = fetch_weather_data(location)
    return jsonify(weather_data)

def fetch_weather_data(location):
    # Use a weather API (e.g., OpenWeatherMap)
    api_key = 'eabbea174efc128186d008c98710ff9c'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(api_url)
    data = response.json()

    return {
        'location': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
    }

if __name__ == '__main__':
    app.run(debug=True)
