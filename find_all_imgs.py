import re

with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Find all img tags and their contexts
img_matches = list(re.finditer(r'<img\b[^>]*>', orig, re.IGNORECASE))
print(f"Found {len(img_matches)} img tags:")
for i, m in enumerate(img_matches):
    tag = m.group(0)
    start = max(0, m.start() - 100)
    end = min(len(orig), m.end() + 100)
    context = orig[start:end].replace("\n", " ").replace("\r", " ")
    print(f"--- IMG #{i+1} ---")
    print("TAG:", tag)
    # Check what section/heading it is under
    heading_before = orig[:m.start()].rfind("<h2")
    if heading_before != -1:
        h2_text = orig[heading_before:orig.find("</h2>", heading_before)+5]
        h2_clean = re.sub(r'<[^>]+>', '', h2_text).strip()
        print("Under H2:", h2_clean)
