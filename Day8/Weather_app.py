import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 404:
        print("City Not Found")

    elif response.status_code == 401:
        print("Invalid API Key")

    elif response.status_code == 200:
        print("\nWeather Information")
        print("-----------------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("Error:", data.get("message"))

except requests.exceptions.ConnectionError:
    print("No Internet Connection")

except requests.exceptions.Timeout:
    print(" Request Timed Out")

except Exception as e:
    print("Something Went Wrong:", e)