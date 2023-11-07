x = int(input("ввести 5-ти значне число:"))
number_1 = x % 10
number_2 = x % 100 // 10
number_3 = x % 1000 // 100
number_4 = x // 1000 % 10
number_5 = x // 10000
print(number_1, number_2, number_3, number_4, number_5)