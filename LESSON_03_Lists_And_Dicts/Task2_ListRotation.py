"""
Задача 2. 
Дана последовательность из N целых чисел и положительное число К. 
Необходимо сдвинуть последовательность на К элементов вправо. 
Сдвиг циклический. 
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Иcходный список = {}".format(list_1))
k = int(input("На сколько элементов вправо будем сдвигать этот список? => "))
k = k%len(list_1)
print("k = {}".format(k))
res = list([0])*10
print("Новый список = {}".format(res))
if k != 0 : 
    for i in range(len(list_1)) : 
        res[(k+i)%len(list_1)] = list_1[i]
else : 
    res = list(list_1)
print("Итоговый список = {}".format(res))

"""
Вариант, разобранный на семинаре
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Иcходный список = {}".format(list_1))
k = int(input("На сколько элементов вправо будем сдвигать этот список? => "))
k = k%len(list_1)
print("k = {}".format(k))
res = list(list_1)
for i in range(k): 
    res.insert(0,res.pop(-1))
print("Итоговый список = {}".format(res))
    