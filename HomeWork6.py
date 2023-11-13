x = [1, 2, 3, 4, 5]
if len(x) >= 1:
    y = x.pop(-1)
    x.insert(0,y)
    print(x)
else:
    print(x)