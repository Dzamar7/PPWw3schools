import html
import re

with open("index.html", "r", encoding="utf-8") as f:
    page_html = f.read()

demo_iframes = [
    'tryhow_css_sidenav_ifr.htm',
    'tryhow_css_sidenav_ifr2.htm',
    'tryhow_js_vertical_tabs_ifr.htm',
    'tryhow_js_topnav_iframe.htm',
    'tryhow_css_bg_change_scroll.htm'
]

for ifr in demo_iframes:
    with open(ifr, "r", encoding="utf-8") as f:
        ifr_content = f.read()
    escaped = html.escape(ifr_content, quote=True)
    # Find iframe with src=ifr
    pattern = rf'(<iframe\b[^>]*src=["\']{re.escape(ifr)}["\'][^>]*)(></iframe>)'
    replacement = rf'\1 srcdoc="{escaped}"\2'
    page_html = re.sub(pattern, replacement, page_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(page_html)

print("Injected srcdoc into all 5 demo iframes!")
