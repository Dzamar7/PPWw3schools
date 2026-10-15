with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

import re

# Find scripts from index 15 to 30
scripts = re.findall(r'<script\b([^>]*)>(.*?)</script>', orig, re.DOTALL | re.IGNORECASE)

for i in range(11, len(scripts)):
    attrs, body = scripts[i]
    print(f"=== SCRIPT #{i+1} attrs='{attrs.strip()}' ===")
    print(body.strip())
    print("\n" + "="*40 + "\n")
