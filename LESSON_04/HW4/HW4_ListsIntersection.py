"""
Даны два неупорядоченных набора целых чисел (возможы повторения). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
Пользователь вводит: 
n - количество элементов 1-го множества
m - количество элементов 2-го множества
Затем элементы множеств
"""
# ВВОД СПИСКОВ ПОЛЬЗОВАТЕЛЕМ : 
# n = int(input("Введите длину 1-го набора целых чисел => "))
# m = int(input("Введите длину 2-го набора целых чисел => "))
# set1 = set([int(input(f"Введите {i+1}-й элемент 1-го набора => ")) for i in range(n)])
# set2 = set([int(input(f"Введите {i+1}-й элемент 1-го набора => ")) for i in range(m)])

# ГОТОВЫЕ СПИСКИ : 
set1 = {1, 4, 2, 3, 1, 8, 10, -12, 0, 10, 5, 2}
set2 = {11, 43, 2, 3, 1, 28, 10, -12, 30, 1, 15, 2}
res_list = list(set1.intersection(set2))
res_list.sort(key = lambda x : int(x))
print(res_list)
 
# Я - М О Л О Д Е Ц !!!!!

# РЕШЕНИЕ, РАЗОБРАННОЕ НА СЕМИНАРЕ: 

n, m = input("Введите количество элементов 1-го и 2-го множества через пробел =>").split()

first = [int(i) for i in input("Введите элементы 1-го множества через пробел => \n").split()]
second = [int(i) for i in input("Введите элементы 2-го множества через пробел => \n").split()]

print(*sorted(set(first).intersection(set(second))))