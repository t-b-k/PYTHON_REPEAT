"""
В школе решили создать три новых математических класса и оборудовать 
кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из 3-х классов. 
Выведите наименьшее число парт, которое нужно приобрести для них. 
"""

print("Задача 2. ")
class1 = int(input("Введите число учащихся 1-го класса => "))
class2 = int(input("Введите число учащихся 2-го класса => "))
class3 = int(input("Введите число учащихся 3-го класса => "))
print(f"Понадобится минимум {int(class1/2+0.5)+int(class2/2+0.5)+int(class3/2+0.5)} парт. ")
print(f"Понадобится минимум {-((-class1)//2+(-class2)//2+(-class3)//2)} парт. ")