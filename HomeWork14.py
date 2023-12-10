my_number = input()
if len(my_number) > 1:
    while int(my_number) > 9:
        number = 1
        for i in range(int(len(my_number))):
            number = number * int(my_number[i])
        my_number = str(number)
    print(my_number)
else:
    print(my_number)






