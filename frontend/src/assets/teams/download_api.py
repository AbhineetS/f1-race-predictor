import urllib.request
import json
import re

teams = {
    "astonmartin": "Aston_Martin_in_Formula_One",
    "williams": "Williams_Grand_Prix_Engineering",
    "sauber": "Sauber_Motorsport",
    "racingbulls": "RB_Formula_One_Team"
}

out_dir = "/Users/abhineetsingh/Downloads/f1-race-predictor/frontend/src/assets/teams/"

for team, page in teams.items():
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page}&prop=images&format=json&imlimit=500"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            pages = data['query']['pages']
            for page_id in pages:
                images = pages[page_id].get('images', [])
                logo_file = None
                for img in images:
                    title = img['title']
                    if 'logo' in title.lower() and title.endswith('.svg'):
                        logo_file = title.replace('File:', '')
                        break
                
                if logo_file:
                    print(f"Found logo for {team}: {logo_file}")
                    svg_url = f"https://en.wikipedia.org/wiki/Special:FilePath/{urllib.parse.quote(logo_file)}"
                    svg_req = urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(svg_req) as svg_res:
                        with open(out_dir + f"{team}.svg", 'wb') as f:
                            f.write(svg_res.read())
                    print(f"Success: {team}")
                else:
                    print(f"No SVG logo found for {team}")
    except Exception as e:
        print(f"Failed {team}: {e}")
