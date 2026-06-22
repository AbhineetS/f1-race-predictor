import requests

def fetch(endpoint):
    return requests.get(f"https://api.openf1.org/v1/{endpoint}").json()

print("Fetching all sessions...")
sessions = fetch("sessions")
if sessions:
    # Get the last 5 sessions
    for s in sessions[-5:]:
        print(s.get("session_key"), s.get("session_name"), s.get("date_start"), s.get("date_end"))
