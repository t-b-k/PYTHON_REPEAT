"""
* Функции
* Модули
* Рекурсия
* Быстрая сортировка
* Сортировка слиянием
"""

# ФУНКЦИЯ - ЭТО ФРАГМЕНТ ПРОГРАММЫ, ИСПОЛЬЗУЕМЫЙ МНОГОКРАТНО

# def function_name(x) : 
      # body Line 1
      #...
      # body Line N
      # optional return

# ПРИМЕР: напишем функцию sumNumbers(n), которая будет суммировать 
# все числа от 1 до N
# ВАЖНО: сколько аргументов функция принимает, столько мы в нее и передаем

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1) : 
#         summa += i
#     print(summa)

# sumNumbers(5)

# ПЕРЕПИШЕМ sumNumbers таким образом, чтобы она возвращала результат 

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1) : 
#         summa += i
#     return summa

# print(sumNumbers(5))

# Наткнувшись на return, интерпретатор возвращает управление из функции
# Если некоторому аргументу функции присвоить значение по умолчанию, 
# то его можно при вызове не передавать: 

# def sumNumbers(n, y = 'Hello!'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1) : 
#         summa += i
#     return summa

# a = sumNumbers(5, "Привет!")
# print(a)

# Можно создавать функции с неопределенным количеством аргументов: 
# def f(*args)

# def sumStr(*args): 
#     print(type(args))
#     res = ''
#     for i in args : 
#         res += i
#     return(res)

# print(sumStr('П', 'ри', 'ве', 'т'))
# print(sumStr(str(1), str(8), str(10), str(2)))

# МОДУЛЬНОСТЬ
# Чтобы не раздувать код, функции, объединенные некоторым общим свойством, 
# принято помещать в отдельные файлы и при необходимости "подцеплять" их к 
# проектам при помощи определенных команд

# Попробуем реализовать данный подход
# Создадим файл с названием module.py

# Р Е К У Р С И Я
# Рекурсия - это функция, которая вызывает сама себя

# При описании рекурсии важно не забыть правильно определить ее базис, 
# то есть условие, при котором она должна перестать вызывать сама себя. 

# РЕШИМ ЗАДАЧУ: 
# Пользователь вводит число N 
# Требуется вывести N первых чисел Фибоначчи

def fib(n) : 
    if n == 1 or n == 2:
        return 1 
    else : 
        return fib(n-1)+fib(n-2)

n = int(input("Введите число N ==> "))
for i in range(1, n+1) : 
    print(fib(i), end=" ")
 







