import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_path = os.path.abspath("index.html")

# Take full page screenshot
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,3000",
    f"--screenshot={os.path.abspath('screenshot_mid.png')}",
    f"file:///{index_path.replace(os.sep, '/')}"
]

subprocess.run(cmd, capture_output=True)
print("Saved screenshot_mid.png")
