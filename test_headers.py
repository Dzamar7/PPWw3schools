import urllib.request

test_urls = [
    "https://www.w3schools.com/adventure/img/mascot-lynx.png",
    "https://www.w3schools.com/howto/img_nature_wide.jpg",
    "https://www.w3schools.com/w3css/img_avatar3.png",
    "https://www.w3schools.com/signup/lynxlogo.svg",
    "https://www.w3schools.com/howto/img_avatar2.png",
]

for url in test_urls:
    # Test with localhost referer
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": "http://localhost:8080/"
    })
    try:
        res = urllib.request.urlopen(req)
        print(f"Referer localhost: {url} -> {res.status}")
    except Exception as e:
        print(f"Referer localhost: {url} -> FAILED: {e}")

    # Test with no referer
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0"
    })
    try:
        res = urllib.request.urlopen(req)
        print(f"No referer: {url} -> {res.status}")
    except Exception as e:
        print(f"No referer: {url} -> FAILED: {e}")
