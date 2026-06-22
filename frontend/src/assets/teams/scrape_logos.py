import urllib.request
import re
import os

teams = {
    "ferrari": "Scuderia_Ferrari",
    "redbull": "Red_Bull_Racing",
    "astonmartin": "Aston_Martin_in_Formula_One",
    "haas": "Haas_F1_Team",
    "williams": "Williams_Grand_Prix_Engineering",
    "sauber": "Sauber_Motorsport",
    "racingbulls": "RB_Formula_One_Team"
}

out_dir = "/Users/abhineetsingh/Downloads/f1-race-predictor/frontend/src/assets/teams/"

for team, page in teams.items():
    try:
        url = f"https://en.wikipedia.org/wiki/{page}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find the first SVG that looks like a logo
            # Example: src="//upload.wikimedia.org/wikipedia/en/thumb/d/df/Scuderia_Ferrari_HP_logo_24.svg/200px-Scuderia_Ferrari_HP_logo_24.svg.png"
            # Or direct link: href="/wiki/File:Scuderia_Ferrari_HP_logo_24.svg"
            
            match = re.search(r'href="/wiki/File:([^"]+\.svg)"', html, re.IGNORECASE)
            if match:
                file_name = match.group(1)
                svg_url = f"https://en.wikipedia.org/wiki/Special:FilePath/{file_name}"
                
                print(f"Downloading {team} from {svg_url}...")
                svg_req = urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(svg_req) as svg_res:
                    with open(os.path.join(out_dir, f"{team}.svg"), 'wb') as f:
                        f.write(svg_res.read())
                print(f"Success: {team}")
            else:
                print(f"No SVG found for {team}")
    except Exception as e:
        print(f"Failed {team}: {e}")
