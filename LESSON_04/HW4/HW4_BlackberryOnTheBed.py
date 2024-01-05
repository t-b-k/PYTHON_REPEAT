"""
В Карелии выращиват чернику. Она растет на круглой грядке, причем кусты высажены по окружности. 
Таким образом, у каждого куста есть два соседних. Всего N кустов. 
К моменту сбора урожая на i-м кусте выросло Ai ягод. 
Собирающий модуль за один заход собирает чернику с трех соседних кустов. 
Напишите программу для определения максимального количества собранных за один заход ягод
"""

# Для решения предлагается использовать список длиной N, поскольку у него есть отрицательная индексация

garden_bed = [int(input(f"Введите урожайность {i+1}-го куста: ")) for i in range(int(input("Сколько кустов растет на грядке? => ")))]
print(garden_bed)
touch_results = [garden_bed[i-2] + garden_bed[i-1] + garden_bed[i] for i in range(len(garden_bed))]
print(touch_results)
touch_results.sort(key = lambda x : x, reverse=1)
print(touch_results)
print(f"Максимально возможный сбор за один подход - {touch_results[0]} ягод(a)!!!")

# Я - М О Л О Д Е Ц !!!

# Решение, разобранное на семинаре: 

n = int(input("Сколько кустов растет на грядке? => "))
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(n) : 
    bush_sum = bushes[i-1] + bushes[i] + bushes[i+1 if i< n-1 else 0]
    if bush_sum > bush_max: 
        bush_max = bush_sum

print("Максимальный сбор с 3-х соседних кустов равен ", bush_max, " ягод.\n")


