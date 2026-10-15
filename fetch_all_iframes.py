import urllib.request

demo_iframes = [
    'tryhow_css_sidenav_ifr.htm',
    'tryhow_css_sidenav_ifr2.htm',
    'tryhow_js_vertical_tabs_ifr.htm',
    'tryhow_js_topnav_iframe.htm',
    'tryhow_css_bg_change_scroll.htm'
]

headers = {"User-Agent": "Mozilla/5.0"}

for ifr in demo_iframes:
    url = f"https://www.w3schools.com/howto/{ifr}"
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req).read()
        with open(ifr, "wb") as f:
            f.write(data)
        print(f"[OK] Downloaded {ifr} ({len(data)} bytes)")
    except Exception as e:
        print(f"[FAIL] {ifr}: {e}")
