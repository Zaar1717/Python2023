
x = [1, 2, 3]
if len(x) % 2 == 0 and len(x) != 0:
    list_1 = x[0:int(len(x)/2)]
    list_2 = x[int((len(x) / 2))::]
    print([list_1, list_2])
elif len(x) % 2 != 0 and len(x) != 0:
    list_1 = x[0:int((len(x) + 1) / 2)]
    list_2 = x[int((len(x) + 1) / 2)::]
    print([list_1, list_2])
else:
    print([[], []])



