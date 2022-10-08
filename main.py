# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988


# from decimal import Decimal

# number = input(str('Вводим число: '))
# raz = (input(str('Вводим разрядность: ')))
# number=Decimal(number)
# number = number.quantize(Decimal(raz))
# print(number)


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54

# out
# [2, 3, 3, 3]

#in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

# def simp_num(number): #функция определения простых чисел до N
#     simple_number = []
#     for j in range(2, number):
#         for i in range(2, j):
#             if j % i == 0:
#                 break
#         else:
#             simple_number.append(j)
#     return simple_number

# def division(num): #функция определения простых множителей N
#     simple_num = simp_num(num)
#     div_num = []
#     for i in range(len(simple_num)):
#         if num % simple_num[i] == 0:
#             div_num.append(simple_num[i])
#     return div_num
# print(division(int(input('Вводите число N:'))))



# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

# import random


# def cr_nln():
#     while True:
#         try:
#             num = int(input('Введите размер списка: '))
#             if num > 0:
#                 list_num = [random.randint(-5, 5) for i in range(num)]
#                 return list_num
#             return "Negative value of the number of numbers!"
#         except ValueError:
#             print('Это не число! Повторим: ')


# list_num = (cr_nln())
# list_out = []
# for i in range(len(list_num)):
#     if list_num.count(list_num[i]) == 1:
#         list_out.append(list_num[i])
# print(f'Исходные значения: {list_num}\nСписок неповторяющихся элементов: {list_out}')


