import requests
import json

url = "https://api.openf1.org/v1/position?session_key=latest"

response = requests.get(url)

data = response.json()

with open("../data/live_positions.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ Data saved successfully!")