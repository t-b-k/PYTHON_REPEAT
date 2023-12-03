"""Задача: 
Требуется найти в массиве A[1..N] наименьший из самых близких по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
"""
# Мое решение:

# qty_of_numbers = int(input("Ведите количество чисел, среди которых мы будем осуществлять поиск => "))
# numbers = [int(input("Введите следующее число => ")) for i in range(qty_of_numbers)]
# number_to_search = int(input("Ближайшее к какому числу мы должны найти>? "))

# res_index = 0
# min_dif = abs(numbers[res_index]-number_to_search)
# for i in range(1, qty_of_numbers) : 
#     compare_result = abs(numbers[i]-number_to_search)
#     if compare_result == min_dif and numbers[i] < numbers[res_index] : 
#         res_index = i
#     elif compare_result < min_dif : 
#         res_index = i
#         min_dif = compare_result

# print(f"Минимальным из ближайших к числу {number_to_search} является число {numbers[res_index]}")

# Разобрано на семинаре: 

from random import randint

# особенность функции randint - она включает и верхнюю, и нижнюю границу
list_nums = [randint(1, 21) for _ in range(int(input("Введите длину списка => ")))]
print(list_nums)
num = int(input("Введите число, ближайшее к которому мы будем искать в нашем списке => "))
right_num = list_nums[0]
for i in list_nums : 
    if abs(num - i) < abs(num - right_num) : 
        right_num = i
print(f"Ближайшим к числу {num} является число {right_num}.")   

# Другой способ: 
res = min(list_nums, key = lambda x : abs(x-num))
print(f"Минимальным из ближайших к числу {num} является число {res}")

# Но в этих вариантах мы находим последнее ближайшее, а не минимальное из ближайших




