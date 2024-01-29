# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt
# Фамилия, Имя, Отчество, Номер_телефона - данные, которые должны находиться в файле. 
# I. Программа должна: 
# 1. Выводить данные
# 2. Сохранять данные в текстовом файле
# 3. Пользователь может ввести одну характеристику для поиска записи в БД (например, имя или фамилию человека)
# 4. Использовать функции (программа не должна быть линейной)
# 5. Должна быть возможность: 
#   - Вывести меню
#   - Просмотреть все записи
#   - Добавить запись
#   - Изменить запись
#   - Удалить запись
#   - Экспортировать справочник
#   - Импортировать справочник
#   - Выход
# II. Когда мы работаем с базой данных, у нас всегда есть ID. Она присваивается каждой записи автоматически. 
# III. Файл с базой данных может не существовать. 
# IV. Для считывания данных и работы с ними будет использоваться глобальная переменная - некоторая структура данных. 
# V. В чем проблема работы с текстовым файлом? Если мы хотим в нем что-то изменить, то это можно сделать единственным образом: 
# полностью стереть все его содержимое и заменить на новое. Других вариантов нет. 
from os import path

file_base = "base.txt"

if not path.exists(file_base) : 
    with open(file_base, "w", encoding = "utf-8") as _  :
        pass
    # Просто создаем файл и ничего не делаем - закрываем. 

last_id = 0
all_data = []

def read_records() : 
    global last_id, all_data
    if last_id : 
        with open(file_base, encoding = "utf-8") as f:
        # В нашем файле лежат строки формата: "ID ФАМИЛИЯ ИМЯ ОТЧЕСТВО ТЕЛЕФОН" - поля разделены пробелами
        # Каждая строка заканчивается "\n"
            all_data = [i.strip() for i in f]
            last_id = all_data[-1][0]
        return all_data
    return []
        # last_id должен быть виден везде => речь идет о глобальной переменной
        # То, что мы пишем в одном файле - это для одного файла. 
        # Если мы хотим использовать переменную в другом модуле, ее надо передавать туда в качестве аргумента. 


def show_all() : 
    if all_data : 
        print(*all_data, sep = "\n")
    else : 
        print("No data")

def add_new_contact() : 
    global last_id, file_base
    array = ["Surname", "Name", "Patronymic", "Phone number"]
    string = ""
    for i in array : 
        string += input(f"Enter {i} ") + " "
    last_id += 1
    with open(file_base, "a", encoding="utf-8") as f : 
        f.write(f"{last_id} {string}\n")



def main_menu(): 
    play = True
    while play : 
        read_records()
        answer = input("Phone book: \n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Import/Export database\n"
                       "7. Exit")
        
        match answer : 
            case "1" : 
                pass
            case "2" : 
                pass
            case "3" : 
                pass
            case "4" : 
                pass
            case "5" : 
                pass
            case "6" : 
                play = False
            case _ : 
                print("Try again!")