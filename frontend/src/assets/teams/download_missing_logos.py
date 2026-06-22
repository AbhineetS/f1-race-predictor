import urllib.request
import os

logos = {
    "williams": "Williams_Racing_2020_logo.svg",
    "sauber": "Kick_Sauber_F1_Team_logo.svg",
    "racingbulls": "RB_Formula_One_Team_logo.svg",
}

for team, filename in logos.items():
    url = f"https://en.wikipedia.org/wiki/Special:FilePath/{filename}"
    output_path = f"/Users/abhineetsingh/Downloads/f1-race-predictor/frontend/src/assets/teams/{team}.svg"
    try:
        print(f"Downloading {team}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Success: {team}")
    except Exception as e:
        print(f"Failed {team}: {e}")
