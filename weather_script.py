import requests
import os

def fetch_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "c502456ddce1cb7670c768853d64e7a0",
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":

    # Replace with your actual API key or set as environment variable
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
    city = input("Enter city name: ")
    try:
        data = fetch_weather(city, API_KEY)
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
    except requests.HTTPError as e:
        print("Failed to fetch weather data:", e)