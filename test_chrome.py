import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_path = os.path.abspath("index.html")

# Run headless chrome to dump dom and see if it crashes or works
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--dump-dom",
    f"file:///{index_path.replace(os.sep, '/')}"
]

p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
print("Dump DOM length:", len(p.stdout))
print("Stderr:", p.stderr[:500] if p.stderr else "None")
