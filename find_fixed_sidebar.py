with open("index.html", "r", encoding="utf-8") as f:
    orig = f.read()

idx = orig.find('howto_css_fixed_sidebar.asp')
# find the one that is in an h2
while idx != -1:
    snippet = orig[idx-50:idx+800]
    if 'h2' in snippet.lower():
        print("FOUND FIXED SIDEBAR CARD:")
        print(snippet)
        break
    idx = orig.find('howto_css_fixed_sidebar.asp', idx+1)
