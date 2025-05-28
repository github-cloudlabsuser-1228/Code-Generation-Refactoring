# use api connection to get weather data
import requests
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return {"error": "City not found or API request failed."}
def display_weather(weather_info):
    if "error" in weather_info:
        print(weather_info["error"])
    else:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description'].capitalize()}")
def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    
    weather_info = get_weather(api_key, city)
    display_weather(weather_info)
if __name__ == "__main__":
    main()