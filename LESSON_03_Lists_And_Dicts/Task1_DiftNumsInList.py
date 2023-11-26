"""
Дан список целых чисел. 
Определить, сколько в нем различных чисел. 
Список может быть задан изначально либо введен пользователем.
"""
counter = int(input("Введите количество элементов в списке чисел: "))
numbers = []
for i in range(counter) : 
    numbers.append(int(input("Введите следующее число => ")))
print(numbers)
num_values = len(set(numbers))
# set не поддерживает индексацию, там элементы хранятся вперемешку
print(set(numbers))
print(num_values)
