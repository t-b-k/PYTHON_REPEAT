# Задача 49.
# Планеты вращаются вокруг Солнца по эллиптическим орбитам. 
# Назовем самой далекой ту, орбита которой имеет наибольшую площадь. 
# Напишите функцию find_farthest_planet(list_of_orbits), которая в списке орбит найдет 
# самую далекую планету. 
# Результатом работы функции должен быть кортеж, содержащий длины полуосей эллипса 
# орбиты самой далекой планеты. 
# Каждая орбита задается кортежем из полуосей ее эллипсоидной орбиты. 
# Площадь эллипса вычисляется по формуле: s = п*a*b, где a и b - полуоси эллипса. 
# При решении задачи используйте списочные выражения. 

# Ввод: [(1,3), (2.5,10), (7,2), (6,6), (4,3)]
# Вывод: 2.5 10

checklist = "[(1,3), (2.5,10), (7,2), (6,6), (4,3)]"
user_input = checklist[1:-1].split(sep=", ")
print(user_input)
lists = list(map(lambda x: x[1:-1].split(","), user_input))
print(lists)
tuples = list(map(lambda x : (float(x[0]), float(x[1])), lists))
print(tuples)
squares = list(map(lambda x : 3.14*float(x[0])*float(x[1]), lists))
print(squares)
max_square = max(list(map(lambda x : 3.14*float(x[0])*float(x[1]) if x[0] != x[1] else 0, lists)))
result = tuples[squares.index(max_square)]
print(*result)

# РЕШЕНИЕ НА СЕМИНАРЕ

init_list = [(1,3), (2.5,10), (7,2), (6,6), (4,3)]

def max_planet (data) : 
    return max({i[0]*i[1]:i for i in init_list if i[0] != i[1]}.items())[1]

print(*max_planet(init_list))


