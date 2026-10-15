import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We can scroll down to 1600px using a small wrapper or evaluate script
# Or set window size to 1280x4000
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,4500",
    f"--screenshot={os.path.abspath('screenshot_full.png')}",
    "http://localhost:8080/"
]

subprocess.run(cmd, capture_output=True)
print("Saved screenshot_full.png")
