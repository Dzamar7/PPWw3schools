import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_path = os.path.abspath("index.html")

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,1024",
    f"--screenshot={os.path.abspath('screenshot_top.png')}",
    f"file:///{index_path.replace(os.sep, '/')}"
]

subprocess.run(cmd, capture_output=True)
print("Screenshot saved to screenshot_top.png, exists:", os.path.exists("screenshot_top.png"))
