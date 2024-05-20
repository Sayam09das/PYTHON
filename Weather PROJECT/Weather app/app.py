from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = '606c6a0fa3b9466d0fb215cacbb83247'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = BASE_URL + 'q=' + city + '&appid=' + API_KEY + '&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            "city": city,
            "temperature": main['temp'],
            "description": weather['description']
        }
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
