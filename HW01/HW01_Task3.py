# Задача 3.
# Счастливым называется билет, в котором сумма первых трех цифр равна сумме трех последних. 
# Требуется написать программу, которая проверяет билет на "счастливость"

number = int(input("Введите номер билета из 6-ти цифр: "))
if number < 0 or number > 999999 : 
    print("Введенное вами число не является номером билета")
sum_last = 0
sum_first = 0
count = 0

while count < 3 : 
    sum_last += number%10
    number = number//10
    count += 1

while count < 6 : 
    sum_first += number%10
    number = number//10
    count += 1

if number > 0 : 
    print("Введенное вами число не является номером билета")
if sum_last == sum_first : 
    print("Ваш билет - счастливый")
else: 
    print("Вам не повезло: ваш билет не является счастливым")