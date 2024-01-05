# Задача № 33. 
# Хакер Василий получил доступ к классному журналу и заменил все свои 
# минимальные оценки на максимальные. 
# Напишите программу, которая делает обратную замену: 
# меняет все максимальные оценки на минимальные
# На входе: количество оценок и сами оценки. 
# На выходе: новые оценки. 

def min_grade(grades) : 
    min_gr = grades[0]
    for i in range(1, len(grades)) : 
        if grades[i] < min_gr : 
            min_gr = grades[i]
    return min_gr

def max_grade(grades) : 
    max_gr = grades[0]
    for i in range(1, len(grades)) : 
        if grades[i] > max_gr : 
            max_gr = grades[i]
    return max_gr

grades = [int(c) for c in input("Введите оценки через пробел => ").split()]
lowest = min_grade(grades)
highest = max_grade(grades)
new_grades = [grades[i] if grades[i] != highest else lowest for i in range(len(grades))]
print(*new_grades)
