import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

dark_matches = re.findall(r'<[^>]+(?:dark|theme|toggle)[^>]*>', orig, re.IGNORECASE)
print(f"Theme toggle matches: {len(dark_matches)}")
for m in dark_matches[:10]:
    if "theme" in m.lower() or "mode" in m.lower():
        print(" ", m)
