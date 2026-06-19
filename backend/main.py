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