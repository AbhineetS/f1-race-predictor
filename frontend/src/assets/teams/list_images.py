import urllib.request
import json
import re

teams = {
    "astonmartin": "Aston_Martin_in_Formula_One",
    "williams": "Williams_Grand_Prix_Engineering",
    "sauber": "Sauber_Motorsport",
    "racingbulls": "RB_Formula_One_Team"
}

for team, page in teams.items():
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page}&prop=images&format=json&imlimit=500"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            pages = data['query']['pages']
            print(f"--- SVGs for {team} ---")
            for page_id in pages:
                images = pages[page_id].get('images', [])
                for img in images:
                    title = img['title']
                    if title.endswith('.svg') or title.endswith('.png'):
                        print(title)
    except Exception as e:
        pass
