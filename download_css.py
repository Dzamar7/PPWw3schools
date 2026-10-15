import os
import urllib.request

css_files = [
    "/lib/topnav/main.v1.0.146.css",
    "/lib/my-learning/main.v1.0.106.css",
    "/lib/pathfinder/main.v1.0.12.css",
    "/w3css/5/w3.css",
    "/lib/w3schools/main.v1.0.5.css",
    "/plus/plans/main.v1.0.3.css",
    "/lib/sparteo.css"
]

base_url = "https://www.w3schools.com"
headers = {"User-Agent": "Mozilla/5.0"}

for c in css_files:
    full_url = base_url + c
    rel_path = c.lstrip("/")
    local_target = os.path.join(".", rel_path.replace("/", os.sep))
    os.makedirs(os.path.dirname(local_target), exist_ok=True)
    try:
        data = urllib.request.urlopen(urllib.request.Request(full_url, headers=headers), timeout=10).read()
        with open(local_target, "wb") as f:
            f.write(data)
        print(f"[SAVED] {full_url} -> {local_target}")
    except Exception as e:
        print(f"[FAIL] {full_url}: {e}")
