"""
Иван Васильевич пришел на рынок, и хочет купить два арбуза: 
самый тяжелый и самый легкий. 
Задано количество арбузов. 
"""

n = int(input("Введите количество арбузов => "))
if n > 1 : 
    min_watmel = 1000
    max_watmel = 0
    for i in range(n) : 
        next_watmel = int(input("Введите вес очередного арбуза => "))
        if next_watmel > max_watmel : 
            max_watmel = next_watmel
        if next_watmel < min_watmel : 
            min_watmel = next_watmel

    print("Самый маленький арбуз весит {} кг, ".format(min_watmel))
    print("Самый большой арбуз весит {} кг. ".format(max_watmel))
elif n == 1: 
    print("На рынке остался единственный арбуз")
else: 
    print("Некорректные исходные данные")