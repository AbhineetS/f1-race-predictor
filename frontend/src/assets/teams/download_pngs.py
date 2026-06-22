import urllib.request

base_url = "https://raw.githubusercontent.com/f1standings/f1standings.github.io/main/assets/img/teams/"
logos = {
    "ferrari": "ferrari.png",
    "mercedes": "mercedes.png",
    "mclaren": "mclaren.png",
    "redbull": "red-bull-racing.png",
    "astonmartin": "aston-martin.png",
    "alpine": "alpine.png",
    "haas": "haas-f1-team.png",
    "williams": "williams.png",
    "sauber": "kick-sauber.png",
    "racingbulls": "rb.png"
}

for team, filename in logos.items():
    url = base_url + filename
    output_path = f"/Users/abhineetsingh/Downloads/f1-race-predictor/frontend/src/assets/teams/{team}.png"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Success: {team}")
    except Exception as e:
        print(f"Failed {team}: {e}")
