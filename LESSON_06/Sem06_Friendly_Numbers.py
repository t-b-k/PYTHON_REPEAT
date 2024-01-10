# Задача № 45. 
# Два различных натуральных числа N и M называются дружественными, если: 
# сумма всех делителей числа N равна M, а сумма всех делителей числа M равна N.
# Для заданного пользователем числа K выведите все пары дружественных чисел,
# каждое из которых не превосходит K. 
# Ввод: 330
# Вывод: 220 и 284

from time import time

# def sum_of_all_divisors (n) : 
#     divisors = [i for i in range(1, int(n//2+1)) if not n%i]
#     # print("Делители числа {}: {}".format(n, divisors))
#     result = 0
#     for i in range(len(divisors)): 
#         result += divisors[i]
#     # print("Сумма всех делителей числа {} равна {}".format(n, result))
#     return result

# sum_of_all_divisors(220)
# sum_of_all_divisors(284)
# k = int(input("Введите число K => "))
# start = time()
# result = [(i, j) for i in range(1, k) for j in range(i+1, k) if sum_of_all_divisors(i) == j and sum_of_all_divisors(j) == i]
# for i in range(len(result)): 
#     print(*result[i])
# print("На вычисления ушло {} мс".format(time()-start))

# РЕШЕНИЕ С СЕМИНАРА: 

k = int(input("Введите число K => ")) 

start = time()

def sum_dev(n) : 
    res = 1
    for i in range(2, int(n**0.5+1)): 
        if n%i == 0 : 
            res = res + i + n//i
    return res

for i in range(1, k): 
    first = sum_dev(i)
    # print(f"first = {first}")
    second = sum_dev(first)
    # print(f"second = {second}")
    if second == i and first < second : 
        print(f"{first} и {second}")

print("На вычисления ушло {} мс".format(time()-start))