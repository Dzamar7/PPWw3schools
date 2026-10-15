import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

base_match = re.search(r'<base[^>]+>', content)
print("Base tag:", base_match.group(0) if base_match else "NONE")

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print("Total imgs in index.html:", len(imgs))
for img in imgs[:15]:
    print(" ", img)

# Also check for css background images or inline styles with url(...)
bg_urls = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', content)
print("Total url(...) in index.html:", len(bg_urls))
for u in set(bg_urls):
    print(" bg:", u)
