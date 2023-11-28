"""
Дан массив целых чисел. 
Написать программу, которая подсчитает количество элементов массива, 
бОльших предыдущего (эл-ма с предыдущим индексом).
Ввод: [0, -1, 5, 2, 3]
Вывод: 2  
Список может быть введен пользователем или задан изначально.
"""

our_list = [1, -5, 6, 10, 3, -6, 0]

# res_list = list()
# for i in range(1,len(our_list)) : 
#     if our_list[i-1] < our_list[i] : 
# res_list.append(our_list[i])

res_list = [our_list[i] for i in range(1,len(our_list)) if our_list[i-1] < our_list[i] ]
print(len(res_list))

