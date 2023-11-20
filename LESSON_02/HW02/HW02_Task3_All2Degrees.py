"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n = int(input("Введите число, вплоть до которого нам следует вывести все степени 2-ки: "))
degree = 0
two_in_degree = 1
while two_in_degree <= n : 
    print("2**{} = {}".format(degree, two_in_degree))
    degree += 1
    two_in_degree *= 2
