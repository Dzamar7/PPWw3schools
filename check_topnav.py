import urllib.request

req = urllib.request.Request("https://www.w3schools.com/lib/topnav/main.v1.0.146.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")
print("Topnav JS length:", len(content))
print("Sample:", content[:300].encode('ascii', errors='replace').decode('ascii'))
