# Задача 26.
# Напишите программу, которая на вход принимает два числа - А и В - 
# и возводит число А в целую степень В

def a_in_degree_b(a, b) : 
    if b == 0 : return 1
    else : 
        return a*a_in_degree_b(a, b-1)
    
a = int(input("Введите основание => "))
b = int(input("Введите показатель => "))
print("{} в степени {} равно {}".format(a, b, a_in_degree_b(a, b)))