with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

import re

# Find all script tags in original_howto.html
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', orig, re.DOTALL | re.IGNORECASE)
print(f"Total script blocks: {len(scripts)}")
for i, s in enumerate(scripts):
    s_clean = s.strip()
    preview = s_clean[:80].replace("\n", " ")
    print(f"Script #{i+1} (len {len(s_clean)}): {preview}...")
