"""
По заданному целому неотрицательному n вычислите n!
Используйте цикл while
"""

n = int(input("Введите натуральное число N => "))
if n >= 0 :
    fact = 1
    temp = n
    while temp > 1 : 
        fact *= temp
        temp -= 1
    print(f"{n}! = ", fact)
else : 
    print("Вы ввели отрицательное число. Оно не является натуральным. ")