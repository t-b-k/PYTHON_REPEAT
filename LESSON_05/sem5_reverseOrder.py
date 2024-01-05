# Задача № 37. 
# Дано натуральное число N и последовательность из N чисел. 
# Требуется вывести эту последовательность в обратном порядке. 
# Запрещается использовать циклы и массивы.

# РЕШЕНИЕ (собственное): 
import random

# def print_in_reverse_order (n) : 
#     num = int(input("Введите число => "))
#     if n == 1 : 
#         print(num, end=" ")
#     else : 
#         print_in_reverse_order (n-1)
#         print(num, end=" ")

# n = int(input("Введите натуральное число N => "))
# print_in_reverse_order(n)
# print("")

# Решение на семинаре (с использованием строки)

# n = input("Введите числа через пробел => ")
# print(n[::-1])

# Решение Алексея Литвинова с помощью рекурсии: 

# def reorder (number, step=1) : 
#     if step == number : 
#         val = input("Введите число => ")
#         print(val, end = " ")
#     else : 
#         val = input("Введите число => ")
#         reorder(number, step+1)
#         print(val, end=" ")

# nums = int(input("Введите количество элементов => "))
# reorder(nums)

# Решение преподавателя: 
def reorder(qty) : 
    if qty == 0 : return ""
    number = input("Введите следующее число => ")
    return reorder(qty-1)+" "+number

quantity = int(input("Введите количество чисел => "))
print(reorder(quantity))
