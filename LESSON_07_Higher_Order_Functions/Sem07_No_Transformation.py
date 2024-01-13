# Задача 47. 
# У вас есть код, который Вы не можете менять: 
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] (или любой другой список)
# transformed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с кодом - задание функции transformation
# Напишите такое лямбда-выражение transformartion, чтобы transformed_values был точной 
# копией values (то есть, values не изменился бы).

transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(list(map(transformation, values)))
