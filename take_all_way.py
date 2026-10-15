import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,10000",
    f"--screenshot={os.path.abspath('screenshot_all_way.png')}",
    "http://localhost:8080/"
]

subprocess.run(cmd, capture_output=True)
print("Saved screenshot_all_way.png")
