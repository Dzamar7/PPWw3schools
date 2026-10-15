import urllib.request
import re

url = "https://www.w3schools.com/howto/default.asp"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")

with open("original_howto.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved original_howto.html, length:", len(html))

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total images found: {len(imgs)}")
for img in imgs[:15]:
    print("  ", img)

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', html)
print(f"Total external scripts: {len(scripts)}")
for s in scripts:
    print("  ", s)

inline_scripts = re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Total inline scripts: {len(inline_scripts)}")
