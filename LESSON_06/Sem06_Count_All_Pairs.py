# Задача № 46. 
# Дан список чисел. 
# Посчитайте, сколько в нем парных значений. 
# Считается, что любые два элемента, равные друг другу, образуют одну пару, 
# которую нужно посчитать. 

# МОЕ РЕШЕНИЕ: 
integers = [1, 2, 3, 2, 5, 6, 3, 3, 5, 7, 6, 5, 8, 5]

count = 0
for i in range(len(integers)-1) : 
    for j in range(i+1,len(integers)) : 
        if integers[i] == integers[j] : 
            count += 1

print(f"Число парных значений в массиве integers = {count}")

# РЕШЕНИЕ НА СЕМИНАРЕ (вообще непонятно, что хотели и что сделали):
list_01 = [1, 2, 3, 2, 5, 6, 3, 3, 5, 7, 6, 5, 8, 5]
dict_list = {}.fromkeys(list_01,0)
print(dict_list)
# Каждому значению исходного списка поставили в соответствие число 0
for i in list_01 : 
    dict_list[i] += 1
print(dict_list)
print([i//2 for i in dict_list.values() if not i%2])