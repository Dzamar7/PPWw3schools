import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

iframes = re.findall(r'<iframe\b[^>]*src=["\']([^"\']+)["\']', orig)
print("All iframes:", iframes)
