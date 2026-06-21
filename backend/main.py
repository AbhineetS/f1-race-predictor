from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DRIVER_MAP = {
    1: ("Max VERSTAPPEN", "Red Bull Racing"),
    44: ("Lewis HAMILTON", "Ferrari"),
    63: ("George RUSSELL", "Mercedes"),
    4: ("Lando NORRIS", "McLaren"),
    81: ("Oscar PIASTRI", "McLaren"),
    16: ("Charles LECLERC", "Ferrari"),
    55: ("Carlos SAINZ", "Williams"),
    14: ("Fernando ALONSO", "Aston Martin"),
    18: ("Lance STROLL", "Aston Martin"),
    10: ("Pierre GASLY", "Alpine"),
    31: ("Esteban OCON", "Haas"),
    23: ("Alex ALBON", "Williams"),
    22: ("Yuki TSUNODA", "Red Bull Racing"),
    27: ("Nico HULKENBERG", "Sauber"),
    87: ("Oliver BEARMAN", "Haas"),
    43: ("Franco COLAPINTO", "Alpine"),
    30: ("Liam LAWSON", "Racing Bulls"),
    6: ("Isack HADJAR", "Racing Bulls"),
    12: ("Kimi ANTONELLI", "Mercedes"),
    11: ("Sergio PEREZ", "Red Bull Racing"),
    77: ("Valtteri BOTTAS", "Sauber"),
}

@app.get("/")
def home():
    return {"message": "F1 Race Predictor API Running"}

@app.get("/positions")
def get_positions():

    url = "https://api.openf1.org/v1/position?session_key=latest"
    response = requests.get(url)
    data = response.json()

    latest_positions = []

    for item in data:
        number = item.get("driver_number")
        if not number: continue

        name, team = DRIVER_MAP.get(
            number,
            (f"Driver {number}", "Unknown Team")
        )

        latest_positions.append({
            "position": item.get("position"),
            "driver_number": number,
            "name": name,
            "team": team
        })

    latest_positions.sort(key=lambda x: x.get("position", 999))

    return latest_positions

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
