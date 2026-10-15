import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

scripts = re.findall(r'<script\b([^>]*)>(.*?)</script>', orig, re.DOTALL | re.IGNORECASE)

print(f"Total scripts: {len(scripts)}")
for i, (attrs, body) in enumerate(scripts):
    body_clean = body.strip()
    if "src=" in attrs:
        print(f"[{i+1}] EXTERNAL: {attrs.strip()}")
    else:
        print(f"[{i+1}] INLINE ({len(body_clean)} chars):")
        print("--- START ---")
        print(body_clean[:300])
        print("--- END ---")
