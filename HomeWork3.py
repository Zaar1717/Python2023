x = int(input("ввести 5-ти значне число:"))
number_1 = x % 10
number_2 = x % 100 // 10
number_3 = x % 1000 // 100
number_4 = x // 1000 % 10
number_5 = x // 10000
return_number = (number_1 * 10000) + (number_2 * 1000) + (number_3 * 100) + (number_4 * 10) + number_5
print(return_number)
