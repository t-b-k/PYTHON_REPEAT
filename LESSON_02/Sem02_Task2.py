"""
Пусть дано А - одно из чисел Фибоначчи. 
Надо определить, каким по счету в ряду чисел Фибоначчи оно является
Числа Фибоначчи: 
№       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18   19   20
Число   0   1   1   2   3   5   8   13  21  34  55  89  144 233 377 610 987 1597 2584 4181   
"""

a = int(input("Введите неотрицательное целое число => "))
prev_fib = 0
current_fib = 1

next_fib = prev_fib + current_fib
num = 2
while next_fib < a : 
    prev_fib = current_fib
    current_fib = next_fib
    next_fib = prev_fib + current_fib
    num += 1

if current_fib != a : 
    if prev_fib == a : 
        num -= 1
    elif next_fib == a: 
        num += 1
    else: 
        print("Данное число не является числом Фибоначчи")
        num = 0

if (num != 0) : 
    print(f"Число {a} является числом Фибоначчи с номером {num}")
    


