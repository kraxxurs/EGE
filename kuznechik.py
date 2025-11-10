from turtle import*

# 7369
coords = set()
for i in range(27):
    fd(5)
    if pos() in coords:
        coords.remove(pos())
    else: 
        coords.add(pos())
    bk(3)
    if pos() in coords:
        coords.remove(pos())
    else: 
        coords.add(pos())
    bk(3)

print(len(coords))