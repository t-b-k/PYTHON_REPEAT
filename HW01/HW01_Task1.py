"""
Найдите сумму цифр 3-значного числа
"""

"""
Комментарий: счит
"""

number = int(input("Введите 3-значное число => "))
if number < 100 or number > 999: 
    print("Вы ввели недопустимые данные")
else: 
    sum = 0
    while number > 0 : 
        rest = number%10
        number = number//10
        sum += rest
    print("Сумма цифр заданного Вами числа равна ", sum)

