import urllib.request

for ifr in ["tryhow_css_sidenav_ifr.htm", "tryhow_css_sidenav_ifr2.htm"]:
    url = f"https://www.w3schools.com/howto/{ifr}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req).read()
        print(f"[OK] {ifr} size: {len(data)}")
        with open(ifr, "wb") as f:
            f.write(data)
    except Exception as e:
        print(f"[FAIL] {ifr}: {e}")
