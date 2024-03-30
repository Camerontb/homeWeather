import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Access the API and application keys
api_key = os.getenv("AMBIENT_WEATHER_API_KEY")
application_key = os.getenv("AMBIENT_WEATHER_APPLICATION_KEY")



url = f"https://api.ambientweather.net/v1/devices?apiKey={api_key}&applicationKey={application_key}"

response = requests.get(url)
print(response.text)
