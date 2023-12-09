import string
my_string = input('')
my_list = my_string[0]
for i in range(ord(my_string[0])+1, ord(my_string[-1])+1):
    my_letter = chr(i)
    my_list = my_list + my_letter
print(my_list)


