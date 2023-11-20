x = [1,0,2,0,3,4]
lst1 = []
lst2 = []
for el in x:
    if el == 0:
        lst1.insert(0,el)
    else:
        lst2.insert(len(lst2),el)
print(lst2 + lst1)
