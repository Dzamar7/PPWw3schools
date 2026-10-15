import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Scroll and take screenshot from mid to bottom
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,6000",
    f"--screenshot={os.path.abspath('screenshot_bottom.png')}",
    "http://localhost:8080/"
]

subprocess.run(cmd, capture_output=True)
print("Saved screenshot_bottom.png")
