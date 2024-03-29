# Задача. 
# Напишите функцию print_operatoin_table(operation, number_of_rows, number_of_columns), 
# вычисляющую значение элемента по номеру строки и номеру столбца и выводяющая итоговую таблицу на печать. 
# Аргументы number_of_rows, number_of_columns задают количество строк и столбцов в результирующей таблице. 
# Нумерация строк и столбцов идет с единицы. 

def operation (x, y) : 
    return x*y

def operation_table (op, rn, cn) : 
    return [[op(i, j) for j in range(1, cn+1)] for i in range(1, rn+1)]

def print_operation_table (op_table) : 
    for i in range(len(op_table)) : 
        print(*op_table[i])

print_operation_table(operation_table(operation, 3, 4))

# РЕШЕНИЕ С ПРЕПОДАВАТЕЛЕМ: 

def print_operation_table (operation, num_rows = 6, num_columns = 6) : 
    for i in range(1, num_columns+1) : 
        for j in range(1, num_rows+1) :
            print(f"{operation(i,j):4}", end = " ")
        print()

print_operation_table(lambda x, y: x*y) 