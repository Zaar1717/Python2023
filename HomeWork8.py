lst = [1, 2 ,3]
x = 0
if len(lst) > 0:
    for i in range(0, len(lst), 2):
        x = x + lst[i]
    print(x * lst.pop())
else:
    print(0)



