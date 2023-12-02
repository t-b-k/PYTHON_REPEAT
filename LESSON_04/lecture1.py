# for i in 'c', 4, -13.7, "весло" : 
#     print(i)

# СПИСКИ. СОЗДАНИЕ. ВЫВОД. 
list_1 = []  # создастся пустой список
list_1 = list() # создастся пустой список
list_1 = [1, 3, 'v', "test", True]  # создастся список из 5-ти разнотипных элементов

# print(list_1)
# print(*list_1)

# for i in list_1: 
#     print(i)

# print(type(list_1))
# print(len(list_1))

# for i in range(len(list_1)) : 
#     print(list_1[i])

# Добавление значения в список
# В конец списка
print(list_1.append(8))
list_1.append(0)
print(list_1)
# На определенную позицию: insert(<индекс позиции>, <значение>)
print(list_1.insert(3, "test1")) # будете выведено None, так как данная функция ничего не возвращает
print(list_1)

# Удаление последнего элемента
# Функция pop (возвращает удаленный последний элемент)
print(list_1.pop())
# ... или элемент с определенным индексом: 
a = list_1.pop(3)
print(a)
print(list_1)

# К спискам также применимы СРЕЗЫ: 
print(list_1[:])
print(list_1[-1])
print(list_1[-5:-1])
print(list_1[:4:2])
print(list_1[1:6:2])

#   К О Р Т Е Ж ('tuple')
# ---------------------------------------------------------------------------
# Кортеж - это неизменяемый список. 
# Он занимает меньше места в памяти и быстрее работает по сравнению со списком. 
# Элементы кортежа заключаются в круглые скобки. 

# СОЗДАНИЕ КОРТЕЖА
print("Кортеж - это неизменяемый список: он гарантирует нам сохранность своих элементов.")
print("Кортеж можно использовать, к примеру, для хранения паролей. ")
print("Примеры работы с кортежами: ")
print("Создание пустого кортежа: t = ()")
t = ()
print(t)
print("t = (1)\nprint(t)\nprint(type(t)) => ")
t = (1)
print(t)
print(type(t))
print("t = (1, )\nprint(t)\nprint(type(t)) => ")
t = (1, )
print(*t)
print(type(t))
print("Длина кортежа t равна ", len(t))
t = (24, 6, 1969)
print("Переменная t имеет тип ", type(t))
print("Я родилась ", "{}-{}-{}".format(t[0], t[1], t[2]))

# Использование кортежа для множественного присваивания: 

a, b = 1, 2
print("a = ", a, ", b = ", b)
a = b = 1
print("a = ", a, ", b = ", b)

# Можно значения элементов кортежа одним оператором присвоить различным переменным: 
# (это называется распаковкой кортежа)
a, b, c = t
print(a, b, c)

v = (1, 2, 3, 4, 5)
print(type(v))

# С Л О В А Р И
# --------------------------------------------------------------------------------------
# Словари - неупорядоченные коллекции произвольных элементов с доступом по ключу
# В списках в качестве ключа используются неотрицательные целые числа - индексы элементов. 
# В словарях в качестве ключа могут выступать значения примитивных типов
# Элементы словаря заключаются в фигурные скобки. 

# Создание пустого словаря: 
d = {}
d = dict()

# Добавление элемента в словарь: 
d['password'] = 'qwerty'
print("d = ", d)
print("d has type ", type(d))
print("Добавим еще одно значение в словарь: d[\"login\"] = \"t-b-k\"")
d['login'] = 't-b-k'
print("d = ", d)

dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print("dictionary = ", dictionary)
for item in dictionary : 
    print("{} : {}".format(item, dictionary[item]))
dictionary[85] = 98998
print("dictionary = ", dictionary)
del dictionary[85]
for item in dictionary :
    print(item)
for k, v in dictionary.items() : 
    print(k, v)
print(type(dictionary.items())) # Class "dict_items": список кортежей (<ключ>, <значение>)
print(dictionary.items())

# М Н О Ж Е С Т В А
#-------------------------------------------------------------------------------------------
# Множество - это набор разных элементов данных (не обязательно одного типа). 
# Ко множествам применимы традиционные математические операции: 
# объединение, пересечение, разность. 

colors = {'red', 'green', 'blue'}
print("Множество colors = {}".format(colors))
print("Выполним операцию colors.add('red')")
colors.add('red')
print("Множество colors = {}".format(colors), " - ничего не изменилось")

print("Выполним операцию colors.add('grey')")
colors.add('grey')
print("Множество colors = {}".format(colors), " - добавился элемент 'grey', поскольку его не было в нашем множестве цветов ")
print("Обратите внимание!!! \nНе в конец и не по алфавиту, поскольку порядок хранения элементов множества в памяти является случайным. ")
print("Выполним операцию print(colors.remove('green')")
print(colors.remove('green'), " - эта операция ничего не возвращает, только изменяет множество: ")
print(colors)
print("Еще раз выполним операцию print(colors.remove('green')")
print("Получим ошибку, поскольку такой элемент уже отсутствует в множестве. ")
print("Выполним операцию print(colors.discard('green'))")
print(colors.discard('green'), ". Она вернет None.")
print("Если мы не хотим вылететь из программы при попытке удаления некоторого элемента из множества, ")
print("надо пользоваться функцией discard")
print("Выполним операцию colors.clear(). Она очистит множество: удалит все его элементы: ")
colors.clear()
print("Множество colors = {}".format(colors))

# ОПЕРАЦИИ НАД МНОЖЕСТВАМИ: 
#---------------------------------------------------
# КОПИРОВАНИЕ МНОЖЕСТВА: copy
# ОБЪЕДИНЕНИЕ МНОЖЕСТВ: union
# ПЕРЕСЕЧЕНИЕ МНОЖЕСТВ: intersection
# РАЗНОСТЬ МНОЖЕСТВ: difference
# ЗАМОРОЗКА МНОЖЕСТВА: frozenset

a = {1, 2, 3, 5, 8}
print("a = ", a)
b = {2, 5, 8, 13, 21}
print("b = ", b)
c = a.copy()
print("c = a.copy()", "\nc = ", c, "\na = ", a) 
u = a.union(b)
print("u = a.union(b)", "\nu = ", u) 
i = a.intersection(b)
print("i = a.intersection(b)", "\ni = ", i) 
dl = a.difference(b)
dr = b.difference(a)
print("dl = a.difference(b)", "\ndl = ", dl) 
print("dr = b.difference(a)", "\ndr = ", dr) 
q = a.union(b).difference(a.intersection(b))
print("q = a.union(b).difference(a.intersection(b))", "\nq = ", q) 
z = frozenset(a)
print("z = frozenset(a): ", "\nz = ", z)

# LIST COMPREHENSION (ГЕНЕРАТОР СПИСКА)
#----------------------------------------------------------------------------------------
# List comprehension - это эффективный способ создания списка при помощи оператора for и конструкции if-else. 
# Он работает быстрее любого другого цикла

# ПРИМЕРЫ: 

# list_1 = [<expression> for item in <iterable>]
# list_2 = [<expression> for item in <iterable> if <condition>] 

# Примеры использования: 
# 1. Создать список из четных чисел от 1 до 100

print("Создадим список из четных чисел от 1 до 100: ")
print("list_even = [2*i for i in range(51)] : ")
list_even = [2*i for i in range(1,51)]
print(list_even)
print("list_even = [i for i in range(2, 101, 2)] :")
list_even = [i for i in range(2, 101, 2)]
print(list_even)
print("list_even = [i for i in range(1, 101) if i%2 == 0] :")
list_even = [i for i in range(1, 101) if i%2 == 0]
print(list_even)