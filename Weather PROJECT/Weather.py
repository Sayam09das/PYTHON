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

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        print(f"City {city} not found.")

if __name__ == "__main__":
    main()
