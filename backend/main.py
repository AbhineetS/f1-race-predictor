import requests
import concurrent.futures
import time
import datetime
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

CACHE = {
    "positions": [],
    "session_info": {"error": "Loading live data..."}
}

points_map = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

def fetch_openf1(endpoint, retries=3):
    for _ in range(retries):
        try:
            resp = requests.get(f"https://api.openf1.org/v1/{endpoint}", timeout=20)
            if resp.status_code == 429:
                time.sleep(1)
                continue
            data = resp.json()
            if isinstance(data, list):
                return data
            return []
        except:
            time.sleep(1)
    return []

def resolve_active_session():
    sessions = fetch_openf1("sessions")
    if not sessions:
        return "latest"
        
    current_time_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
    past_sessions = [s for s in sessions if s.get("date_start") and s.get("date_start") < current_time_str]
    if not past_sessions:
        return "latest"
    
    past_sessions.sort(key=lambda x: x["date_start"])
    latest_session = past_sessions[-1]
    is_active = latest_session.get("date_end") and latest_session.get("date_end") > current_time_str
    
    if is_active or latest_session.get("session_name") in ["Race", "Qualifying"]:
        return latest_session.get("session_key", "latest")
    else:
        past_races = [s for s in past_sessions if s.get("session_name") == "Race"]
        if past_races:
            return past_races[-1].get("session_key", "latest")
        return latest_session.get("session_key", "latest")

def update_cache():
    while True:
        try:
            session_key = resolve_active_session()
            
            # --- Update Session Info ---
            session_data = fetch_openf1(f"sessions?session_key={session_key}")
            if session_data:
                session = session_data[0]
                meeting_key = session.get("meeting_key")
                meeting_data = fetch_openf1(f"meetings?meeting_key={meeting_key}") if meeting_key else []
                meeting = meeting_data[0] if meeting_data else {}
                weather_data = fetch_openf1(f"weather?session_key={session_key}")
                latest_weather = weather_data[-1] if isinstance(weather_data, list) and weather_data else {}
                laps_data = fetch_openf1(f"laps?session_key={session_key}&driver_number=1")
                latest_lap = laps_data[-1].get("lap_number") if isinstance(laps_data, list) and laps_data else None
                
                CACHE["session_info"] = {
                    "session_name": session.get("session_name"),
                    "circuit_short_name": session.get("circuit_short_name"),
                    "meeting_name": meeting.get("meeting_name"),
                    "country_code": meeting.get("country_code"),
                    "country_flag": meeting.get("country_flag"),
                    "air_temperature": latest_weather.get("air_temperature"),
                    "track_temperature": latest_weather.get("track_temperature"),
                    "humidity": latest_weather.get("humidity"),
                    "wind_speed": latest_weather.get("wind_speed"),
                    "lap_number": latest_lap,
                    "date_start": meeting.get("date_start"),
                    "date_end": meeting.get("date_end"),
                    "location": meeting.get("location")
                }
            
            # --- Update Positions ---
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                f_drivers = executor.submit(fetch_openf1, f"drivers?session_key={session_key}")
                f_positions = executor.submit(fetch_openf1, f"position?session_key={session_key}")
                drivers_data = f_drivers.result()
                pos_data = f_positions.result()

            if drivers_data and pos_data:
                driver_map = {}
                for d in drivers_data:
                    num = d.get("driver_number")
                    if num:
                        name = d.get("full_name", d.get("name_acronym"))
                        team = d.get("team_name")
                        headshot = d.get("headshot_url")
                        color = d.get("team_colour")
                        if name and team:
                            driver_map[num] = (name, team, headshot, color)

                latest_per_driver = {}
                for item in pos_data:
                    num = item.get("driver_number")
                    if not num or num not in driver_map: 
                        continue
                    if num not in latest_per_driver or item.get("date", "") > latest_per_driver[num].get("date", ""):
                        latest_per_driver[num] = item

                driver_numbers = list(latest_per_driver.keys())
                
                def fetch_driver_data(num):
                    laps = fetch_openf1(f"laps?session_key={session_key}&driver_number={num}")
                    intervals = fetch_openf1(f"intervals?session_key={session_key}&driver_number={num}")
                    return num, laps, intervals

                driver_laps = {}
                driver_gaps = {}
                winner_total_time = 0
                winner_num = None

                for num, item in latest_per_driver.items():
                    if item.get("position") == 1:
                        winner_num = num
                        break

                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                    futures = {executor.submit(fetch_driver_data, num): num for num in driver_numbers}
                    for future in concurrent.futures.as_completed(futures):
                        num, laps, intervals = future.result()
                        max_ln = 0
                        for lap in laps:
                            ln = lap.get("lap_number")
                            if ln and ln > max_ln:
                                max_ln = ln
                        driver_laps[num] = max_ln

                        if num == winner_num:
                            winner_total_time = sum([lap.get("lap_duration", 0) for lap in laps if lap.get("lap_duration")])

                        latest_gap = None
                        latest_date = ""
                        for interval in intervals:
                            gap = interval.get("gap_to_leader")
                            date = interval.get("date", "")
                            if gap is not None and date > latest_date:
                                latest_gap = gap
                                latest_date = date
                        driver_gaps[num] = {"gap": latest_gap, "date": latest_date}

                def format_time(seconds):
                    if not seconds: return ""
                    h = int(seconds // 3600)
                    m = int((seconds % 3600) // 60)
                    s = seconds % 60
                    if h > 0:
                        return f"{h}:{m:02d}:{s:06.3f}"
                    return f"{m}:{s:06.3f}"

                winner_time_str = format_time(winner_total_time)

                latest_positions = []
                for number, item in latest_per_driver.items():
                    name, team, headshot, color = driver_map[number]
                    pos = item.get("position")
                    
                    laps = driver_laps.get(number, None)
                    gap_info = driver_gaps.get(number)
                    gap = gap_info["gap"] if gap_info else None

                    if pos == 1:
                        time_retired = winner_time_str
                    else:
                        winner_laps = driver_laps.get(winner_num, laps)
                        if winner_laps is not None and laps is not None and winner_laps > laps:
                            laps_behind = winner_laps - laps
                            time_retired = f"+{laps_behind} lap{'s' if laps_behind > 1 else ''}"
                        else:
                            if isinstance(gap, (int, float)):
                                time_retired = f"+{gap:.3f}s" if gap else ""
                            elif gap:
                                time_retired = str(gap)
                            else:
                                time_retired = ""

                    pts = points_map.get(pos, "")

                    latest_positions.append({
                        "position": pos,
                        "driver_number": number,
                        "name": name,
                        "team": team,
                        "headshot_url": headshot,
                        "team_colour": color,
                        "laps": laps,
                        "time_retired": time_retired,
                        "pts": pts
                    })

                latest_positions.sort(key=lambda x: x["position"])
                unique_positions = []
                seen = set()
                for lp in latest_positions:
                    if lp["driver_number"] not in seen:
                        seen.add(lp["driver_number"])
                        unique_positions.append(lp)
                        
                CACHE["positions"] = unique_positions[:22]

        except Exception as e:
            print("Cache update failed:", e)
        
        # Sleep for 15 seconds before refreshing cache
        time.sleep(15)

@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=update_cache, daemon=True)
    thread.start()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "F1 Race Predictor API Running"}

@app.get("/positions")
def get_positions():
    return CACHE["positions"]

@app.get("/session-info")
def get_session_info():
    return CACHE["session_info"]

@app.get("/sessions")
def get_sessions(country: str = None, year: int = None):
    # Added by EliteCoder313 to track track layout and year metadata
    url = "https://api.openf1.org/v1/sessions"
    
    # Build query parameters based on what user wants to filter
    params = {}
    if country:
        params["country_name"] = country
    if year:
        params["year"] = year
        
    response = requests.get(url, params=params)
    return response.json()
