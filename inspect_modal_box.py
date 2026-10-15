with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

idx = orig.find('howto_css_modals.asp')
if idx != -1:
    print(orig[idx:idx+1500])
