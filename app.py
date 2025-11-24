import requests
from datetime import datetime

api_key = '4ea42183b357d0ff43769a951b5533d3'

user_input = input("Enter city: ")
current_date = datetime.now().strftime("%A, %B %d, %Y")

weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

print(f"Date: {current_date}")
print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}°F")