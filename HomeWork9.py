import random
lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(0, 9))
print([lst[0], lst[2], lst[len(lst) - 2]])
