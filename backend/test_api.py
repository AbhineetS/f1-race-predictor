import requests

session_key = "latest"
laps_resp = requests.get(f"https://api.openf1.org/v1/laps?session_key={session_key}", timeout=10)
laps = laps_resp.json()

intervals_resp = requests.get(f"https://api.openf1.org/v1/intervals?session_key={session_key}", timeout=10)
intervals = intervals_resp.json()

print(f"Fetched {len(laps)} laps and {len(intervals)} intervals.")

driver_laps = {}
for lap in laps:
    d = lap.get("driver_number")
    ln = lap.get("lap_number")
    if d and ln:
        if d not in driver_laps or ln > driver_laps[d]:
            driver_laps[d] = ln

driver_gaps = {}
for interval in intervals:
    d = interval.get("driver_number")
    gap = interval.get("gap_to_leader")
    date = interval.get("date")
    if d and gap is not None:
        if d not in driver_gaps:
            driver_gaps[d] = {"gap": gap, "date": date}
        else:
            if date > driver_gaps[d]["date"]:
                driver_gaps[d] = {"gap": gap, "date": date}

print("Max laps per driver:", driver_laps)
print("Latest gap for Lewis (44):", driver_gaps.get(44))
print("Latest gap for George (63):", driver_gaps.get(63))
