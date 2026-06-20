import requests
import json

# --- 1. Drivers endpoint ---
drivers_url = "https://api.openf1.org/v1/drivers"
drivers_data = requests.get(drivers_url).json()
with open("data/drivers.json", "w") as f:
    json.dump(drivers_data, f, indent=2)
print(f"Saved {len(drivers_data)} driver records to data/drivers.json")

# --- 2. Position endpoint ---
position_url = "https://api.openf1.org/v1/position"
position_data = requests.get(position_url).json()
with open("data/positions.json", "w") as f:
    json.dump(position_data, f, indent=2)
print(f"Saved {len(position_data)} position records to data/positions.json")

# --- 3. Sessions endpoint ---
sessions_url = "https://api.openf1.org/v1/sessions"
sessions_data = requests.get(sessions_url).json()
with open("data/sessions.json", "w") as f:
    json.dump(sessions_data, f, indent=2)
print(f"Saved {len(sessions_data)} session records to data/sessions.json")