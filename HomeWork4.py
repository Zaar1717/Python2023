x = int(input('Please enter first number'))
y = int(input('Please enter second number'))
z = input("Please enter action")
if z == '+':
    print(x+y)
elif z == '-':
    print(x-y)
elif z == '*':
    print(x*y)
elif z == '/' and y != 0:
    print(x/y)
elif y == 0:
    print('you can not divide by 0')
else:
    print('incorrect')
