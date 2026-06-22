from main import get_active_session_key, fetch_openf1
sk = get_active_session_key()
print("Session Key:", sk)
drivers = fetch_openf1(f"drivers?session_key={sk}")
pos = fetch_openf1(f"position?session_key={sk}")
print("Drivers length:", len(drivers))
print("Positions length:", len(pos))
