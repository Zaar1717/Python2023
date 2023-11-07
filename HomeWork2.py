x = int(input("ввести 4-х значне число:"))
number_1 = x // 1000
number_2 = x // 100 % 10
number_3 = x % 100 // 10
number_4 = x % 10
print(number_1, number_2, number_3, number_4, sep='\n')