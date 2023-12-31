"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

"""
Теорема Виета: 
Сумма корней уравления x2 + bx + c = 0 равна второму коэффициенту с противоположным знаком, 
а произведение корней равняется свободному члену.
Получается, что числа X и Y - это корни квадратного уравнения z*z-Sz+P = 0
X = (s - VD)/2
Y = (s + VD)/2, где D = S2-4*P (D - дискриминант)
"""

s = int(input("Чему равна сумма чисел X и Y ? "))
p = int(input("Чему равно произведение чисел X и Y ? "))

d = s**2-4*p
if d < 0 : 
    print("Петя обманул Катю. Таких целых чисел не существует.")
elif d == 0 : 
    print("Петя загадал два одинаковых числа, равных {}".format(s//2))
else: 
    sqrt_d = 1
    while sqrt_d**2 < d : 
        sqrt_d += 1
    if sqrt_d > d : 
        print("Петя обманул Катю. Таких целых чисел не существует.")
    else: 
        print("Петя загадал числа {} и {}.".format((s-sqrt_d)//2, (s+sqrt_d)//2))

"""
РАЗОБРАНО НА СЕМИНАРЕ: 
С ПРОВЕРКОЙ ВРЕМЕНИ ВЫПОЛНЕНИЯ
from time import time
s = int(input("Sum of numbers: "))
p = int(input("Product of numbers: "))
answer = "I didn't guess"
start = time()
d = s**2-4*p
if d >= 0 : 
    x_1 = (s-d**0.5)/2
    x_2 = (s+d**0.5)/2
    if x_1*x_2 == p : 
    answer = f"{x_1}, {x_2}"

print(answer)
print(time()-start)
"""