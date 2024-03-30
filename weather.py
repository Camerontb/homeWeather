

import requests
import json

url = "https://api.ambientweather.net/v1/devices?apiKey=fa3e087e4b974c109e2f3b4c6186054b7e500b8c672f4d3d9d391ca6a5d4c2d5&applicationKey=67b424b006164a53927fcf7482cfbb52c24c7f91ddb04b95be4d2e2ae7dfed5c"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

pretty_json = json.dumps(response.json(), indent=4)
print(pretty_json)