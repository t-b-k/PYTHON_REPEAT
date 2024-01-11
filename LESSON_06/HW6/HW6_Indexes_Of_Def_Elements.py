# Задача 32. 
# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, 9, 0, -5, -5, 7]
#       7 10
# Вывод: [1, 9, 13, 14, 19]

numbers = input("Введите массив чисел в квадратных скобках и через запятую с пробелом => ")[1:-1].split(sep=", ")
print(*numbers)
minimum, maximum = input("Введите нижнюю и верхнюю границы диапазона через пробел => ").split()
print(f"Минимум = {minimum}, максимум = {maximum}")
for i in range(len(numbers)) : 
    print(numbers[i], sep=" ")
result = [i for i in range(len(numbers)) if minimum <= numbers[i] <= maximum]
print(len(result))
print(result)