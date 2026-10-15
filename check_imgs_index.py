import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find all img src
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print("Img sources in index.html:")
for img in set(imgs):
    print(" ", img)
