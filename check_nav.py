import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Find nav buttons in topnav
nav_matches = re.findall(r'<a\b[^>]*navbtn[^>]*>.*?</a>', orig, re.IGNORECASE | re.DOTALL)
print(f"Nav buttons found: {len(nav_matches)}")
for n in nav_matches:
    print(n.replace("\n", " ").strip()[:150])

# Also find id="nav_tutorials", "nav_references", etc.
nav_sections = re.findall(r'id=["\']nav_[^"\']+["\']', orig)
print("Nav sections:", nav_sections)
