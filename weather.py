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

# Parse the response to JSON
data = response.json()

# Use json.dumps to pretty-print the JSON data
pretty_json = json.dumps(data, indent=4)
print(pretty_json)
