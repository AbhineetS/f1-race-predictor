import requests

url = "https://api.openf1.org/v1/position?session_key=latest"

response = requests.get(url)

data = response.json()

print("🏁 Live Driver Positions:\n")

for position in data[:10]:
    print(
        f"Driver Number: {position.get('driver_number')} | Position: {position.get('position')}"
    )