import re
import urllib.request
import urllib.parse

with open("original_howto.html", "r", encoding="utf-8") as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
base_url = "https://www.w3schools.com/howto/"

print("Checking image URLs:")
headers = {"User-Agent": "Mozilla/5.0"}
for img in set(imgs):
    full_url = urllib.parse.urljoin(base_url, img)
    try:
        req = urllib.request.Request(full_url, headers=headers)
        res = urllib.request.urlopen(req, timeout=5)
        print(f"[OK {res.status}] {img} -> {full_url}")
    except Exception as e:
        print(f"[FAIL] {img} -> {full_url} ({e})")
