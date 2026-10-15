import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Let's inspect the topnav menu toggle mechanism in W3Schools
# Search for nav_tutorials or openNavItem
matches = re.findall(r'openNavItem|nav_tutorials|open_menu', orig)
print("Matches in HTML:", set(matches))

# Let's see how nav_tutorials is structured
tut_idx = orig.find('id="nav_tutorials"')
if tut_idx != -1:
    print("nav_tutorials element snippet:")
    print(orig[tut_idx-50:tut_idx+250])
