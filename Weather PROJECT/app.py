import turtle
import requests

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

def display_weather(weather_data):
    turtle.clearscreen()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write(f"Weather in {weather_data['city']}", align="center", font=("Arial", 20, "bold"))
    turtle.goto(0, 50)
    turtle.write(f"Temperature: {weather_data['temperature']}°C", align="center", font=("Arial", 16, "normal"))
    turtle.goto(0, 0)
    turtle.write(f"Description: {weather_data['description']}", align="center", font=("Arial", 16, "normal"))
    turtle.hideturtle()

def main():
    city = turtle.textinput("Weather App", "Enter city name:")
    if city:
        weather_data = get_weather(city)
        if weather_data:
            display_weather(weather_data)
        else:
            turtle.clearscreen()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.write(f"City {city} not found.", align="center", font=("Arial", 16, "normal"))
            turtle.hideturtle()

if __name__ == "__main__":
    turtle.speed(0)
    main()
    turtle.done()
