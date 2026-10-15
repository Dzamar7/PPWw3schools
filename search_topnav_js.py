import urllib.request
import re

req = urllib.request.Request("https://www.w3schools.com/lib/topnav/main.v1.0.146.js", headers={"User-Agent": "Mozilla/5.0"})
js = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")

idx = js.find("openNavItem")
if idx != -1:
    print("Found openNavItem at:", idx)
    print(js[max(0, idx-100):min(len(js), idx+300)])
else:
    print("openNavItem not found in topnav JS")
