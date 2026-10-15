import subprocess
import os
import re

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_path = os.path.abspath("index.html")

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--dump-dom",
    f"file:///{index_path.replace(os.sep, '/')}"
]

p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
dom = p.stdout

pag_matches = re.findall(r'<div class="howtopag">(.*?)</div>', dom, re.DOTALL)
print("howtopag elements found:", len(pag_matches))
for i, pm in enumerate(pag_matches):
    clean = pm.strip()[:150].encode('ascii', errors='replace').decode('ascii')
    print(f"Pagination #{i+1}:", clean)

slides = re.findall(r'<div class="mySlides[^"]*"[^>]*style="([^"]*)"', dom)
print("Slides style:", slides)
