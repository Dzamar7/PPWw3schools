with open("original_howto.html", "r", encoding="utf-8") as f:
    orig = f.read()

idx = orig.find('myModal2')
if idx != -1:
    print(orig[idx-100:idx+600])
