import requests
import json


drivers_url = "https://api.openf1.org/v1/drivers?session_key=latest"
drivers_data = requests.get(drivers_url).json()
with open("data/drivers.json", "w") as f:
    json.dump(drivers_data, f, indent=2)
print(f"Saved {len(drivers_data)} driver records to data/drivers.json")


position_url = "https://api.openf1.org/v1/position?session_key=latest"
position_data = requests.get(position_url).json()
with open("data/positions.json", "w") as f:
    json.dump(position_data, f, indent=2)
print(f"Saved {len(position_data)} position records to data/positions.json")


sessions_url = "https://api.openf1.org/v1/sessions?session_key=latest"
sessions_data = requests.get(sessions_url).json()
with open("data/sessions.json", "w") as f:
    json.dump(sessions_data, f, indent=2)
print(f"Saved {len(sessions_data)} session records to data/sessions.json")