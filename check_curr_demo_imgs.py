with open("index.html", "r", encoding="utf-8") as f:
    curr = f.read()

import re
imgs_in_curr = re.findall(r'<img\b[^>]*>', curr)
print(f"Total img tags in current index.html: {len(imgs_in_curr)}")
for i, tag in enumerate(imgs_in_curr):
    if "img_" in tag or "avatar" in tag:
        print(f"[{i+1}] {tag}")
