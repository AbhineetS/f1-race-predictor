from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "F1 Race Predictor API Running"
    }


@app.get("/positions")
def get_positions():
    url = "https://api.openf1.org/v1/position?session_key=latest"
    response = requests.get(url)
    return response.json()

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