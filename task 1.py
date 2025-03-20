import requests


def get_weather(city_name, api_key):

    base_url = "http://api.openweathermap.org/data/2.5/weather"


    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:

        response = requests.get(base_url, params=params)
        response.raise_for_status()


        weather_data = response.json()


        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]


        print(f"Weather in {city_name.capitalize()}:")
        print(f"  Condition: {weather.capitalize()}")
        print(f"  Temperature: {temperature}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Pressure: {pressure} hPa")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to get weather data. Details: {e}")
    except KeyError:
        print("Error: Invalid data received from the API.")



API_KEY = "3538c7353ea6924c8139a1e8b5aa90a2"
city = "Lusaka"

get_weather(city, API_KEY)