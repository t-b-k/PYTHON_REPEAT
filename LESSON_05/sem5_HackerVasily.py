# Задача № 33. 
# Хакер Василий получил доступ к классному журналу и заменил все свои 
# минимальные оценки на максимальные. 
# Напишите программу, которая делает обратную замену: 
# меняет все максимальные оценки на минимальные
# На входе: количество оценок и сами оценки. 
# На выходе: новые оценки. 

# def min_grade(grades) : 
#     min_gr = grades[0]
#     for i in range(1, len(grades)) : 
#         if grades[i] < min_gr : 
#             min_gr = grades[i]
#     return min_gr

# def max_grade(grades) : 
#     max_gr = grades[0]
#     for i in range(1, len(grades)) : 
#         if grades[i] > max_gr : 
#             max_gr = grades[i]
#     return max_gr

# grades = [int(c) for c in input("Введите оценки через пробел => ").split()]
# lowest = min_grade(grades)
# highest = max_grade(grades)
# new_grades = [grades[i] if grades[i] != highest else lowest for i in range(len(grades))]
# print(*new_grades)

# Решение на семинаре: 

# import random

# n = int(input("Введите количество оценок: "))
# array = [random.randint(1,5) for i in range(n)]
# print(*array)
# grade_min = min(array)
# grade_max = max(array)
# final_grades = [grade_min if i == grade_max else i for i in array]
# print(*final_grades)

# Вариант с рекурсией: 
import random
n = int(input("Введите количество оценок: "))
array = [random.randint(1,5) for i in range(n)]
print(*array)
grade_min = min(array)
grade_max = max(array)

def maxsToMins (list, ind) : 
    if list[ind] == grade_max : 
        list[ind] = grade_min
    if ind == 0 : 
        return list
    else : 
        return maxsToMins(list, ind-1)

result = maxsToMins(array, len(array)-1)
print(*result)
