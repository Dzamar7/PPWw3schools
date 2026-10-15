import urllib.request

req = urllib.request.Request("https://www.w3schools.com/howto/howto.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")
with open("howto.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Downloaded howto.js, length:", len(content))
print(content[:500])
