import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Screenshot of http://localhost:8080/
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,2400",
    f"--screenshot={os.path.abspath('screenshot_server.png')}",
    "http://localhost:8080/"
]

subprocess.run(cmd, capture_output=True)
print("Saved screenshot_server.png")
