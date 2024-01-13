# Задача 51. 
# Напишите функцию same_by(characteristics, ojects), которая проверяет, все ли объекты 
# удовлетворяют некоторому свойству (характеристике) и возвращает True, если все, и False, если не все. 
# Для пустого набора объектов возвращает True
# characteristics - это функция, которая принимает объект и возвращает его характеристику


# values = [0, 2, 10, 6]
values = []

def same_by(characteristics, objects) :
    res = set(map(lambda x: characteristics(x), objects))
    if len(res) < 2 : 
        return True
    else : 
        return False
    
def characteristics (x) : 
    return x%2

if same_by (characteristics, values) : 
    print("Yes")
else : 
    print("No")