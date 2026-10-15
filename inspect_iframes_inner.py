import os
import re

demo_iframes = [
    'tryhow_css_sidenav_ifr.htm',
    'tryhow_css_sidenav_ifr2.htm',
    'tryhow_js_vertical_tabs_ifr.htm',
    'tryhow_js_topnav_iframe.htm',
    'tryhow_css_bg_change_scroll.htm'
]

for ifr in demo_iframes:
    with open(ifr, "r", encoding="utf-8") as f:
        c = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    css = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', c)
    print(f"--- {ifr} ---")
    if imgs: print("  Images:", imgs)
    if css: print("  CSS:", css)
    if not imgs and not css: print("  (Self-contained HTML/CSS/JS)")
