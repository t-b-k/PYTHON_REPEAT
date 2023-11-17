"""
Требуется определить, можно ли от шоколадки размером m х n долек
отломить к долек, если разрешается сделать только один разлом по прямой
"""

m = int(input("Введите m => "))
n = int(input("Введите n => "))
k = int(input("Введите k => "))

result = k > 0 and k < m*n and (k%m == 0 or k%n == 0)
if result : 
    print("Можно")
else: 
    print("Нельзя")