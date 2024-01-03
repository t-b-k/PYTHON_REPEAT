# Быстрая сортировка реализует стратегию "Разделяй и властвуй"
# Предположим, два друга решили поиграть в игру: один загадывает число от 0 до 100, 
# а другой должен угадать, какое число он загадал. 

def quickSort(array) : 
    if len(array) <= 1 : 
        return array
    pivot = array[0]
    # в 1-й массив будем класть все элементы, которые меньше 1-го, 
    # во 2-й - все элементы, которые больше 1-го

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10, 5, 7, 3, 0, 9, 33]))
