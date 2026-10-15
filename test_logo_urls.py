import urllib.request
import re

# Check if there is an svg logo on w3schools
for test_url in [
    "https://www.w3schools.com/images/w3schools.png",
    "https://www.w3schools.com/images/w3schools_logo_436_2.png",
    "https://www.w3schools.com/favicon.ico",
    "https://upload.wikimedia.org/wikipedia/commons/a/a0/W3Schools_logo.svg",
    "https://www.w3schools.com/lib/w3schools32.png"
]:
    try:
        req = urllib.request.Request(test_url, headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req)
        print(f"[OK {res.status}] {test_url}")
    except Exception as e:
        print(f"[FAIL] {test_url}: {e}")
