import os
import urllib.request
import urllib.parse
import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', orig)
base_url = "https://www.w3schools.com/howto/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

downloaded = set()
for img_src in set(imgs):
    if not img_src or img_src.startswith("data:"):
        continue
    full_url = urllib.parse.urljoin(base_url, img_src)
    # Determine local filename
    # e.g. /adventure/img/mascot-lynx.png -> adventure/img/mascot-lynx.png
    parsed = urllib.parse.urlparse(full_url)
    rel_path = parsed.path.lstrip("/")
    
    # Also if it's in howto/, e.g. howto/img_nature.jpg -> can also save as img_nature.jpg in root
    filename = os.path.basename(parsed.path)
    
    # Create local directories if needed
    local_target = os.path.join(".", rel_path.replace("/", os.sep))
    os.makedirs(os.path.dirname(local_target), exist_ok=True)
    
    try:
        req = urllib.request.Request(full_url, headers=headers)
        data = urllib.request.urlopen(req, timeout=10).read()
        with open(local_target, "wb") as f:
            f.write(data)
        # Also if it's in howto/ or an important image, save a copy directly in root
        if "howto/" in parsed.path or parsed.path.startswith("/images/") or parsed.path.startswith("/w3css/"):
            with open(filename, "wb") as f:
                f.write(data)
        print(f"[SAVED] {full_url} -> {local_target} & {filename}")
        downloaded.add(img_src)
    except Exception as e:
        print(f"[ERROR] {full_url}: {e}")

print(f"\nTotal images downloaded: {len(downloaded)}")
