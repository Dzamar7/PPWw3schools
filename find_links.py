import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

links = re.findall(r'<link\b[^>]*>', orig, re.IGNORECASE)
print(f"Total link tags: {len(links)}")
for l in links:
    if "stylesheet" in l.lower() or "icon" in l.lower():
        print(l.strip())
