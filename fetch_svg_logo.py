import urllib.request

req = urllib.request.Request("https://upload.wikimedia.org/wikipedia/commons/a/a0/W3Schools_logo.svg", headers={"User-Agent": "Mozilla/5.0"})
svg_content = urllib.request.urlopen(req).read().decode("utf-8")
print("SVG length:", len(svg_content))
print(svg_content[:500])
with open("w3schools_logo.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
