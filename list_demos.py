with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Let's search for all <h2> or demo titles in the main content
import re
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', orig)
print("H2 titles found in original_howto.html:")
for i, h in enumerate(h2s):
    print(f"{i+1}. {h}")
