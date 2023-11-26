"""
Оттепель - это период, в течение которого среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Требуется определить продолжительность самой длинной оттепели в заданном периоде длиной N дней
"""

n = int(input("Введите продолжительность анализируемого периода в днях: "))
warm_period = 0
max_warm_period = 0
for i in range(n) : 
    temp = int(input(f"Введите среднесуточную температуру в {i+1}-й день периода: "))
    if temp > 0 : 
        warm_period += 1
    else: 
        if warm_period > 0 : 
            if warm_period > max_warm_period : 
                max_warm_period = warm_period
                warm_period = 0

print(f"Максимальная оттепель длилась {max_warm_period} дня(ей)")


