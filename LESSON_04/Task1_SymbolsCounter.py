# Задача 1. 
# Напишите программу, которая принимает на вход строку и отслеживает, 
# сколько раз в ней встречается каждый символ. 
# Количество повторов добавляется к символам с помощью постфикса формата "_n".
# *Для решения задачи используйте функцию split()
# Пример: aaabcaadcdd
# Ответ:  aa_1a_2bca_3a_4dc_1d_1d_2

init_str = "aaabcaadcdd"
str_list = list(init_str)
res_str = ""
symbols = list(set(init_str))
qties = dict()
print(dir(qties))
for ch in symbols : 
    qties[ch] =0
print(qties)

for let in init_str : 
    res_str += let
    qties[let] += 1
    if qties[let] > 1 : 
        res_str += "_" + str(qties[let]-1)
print(res_str) 

# РЕШЕНИЕ С СЕМИНАРА
res_str = ""
my_dict = {}
for ch in init_str : 
    if ch in my_dict : 
        res_str += f"{ch}_{my_dict[ch]}"
    else: 
        res_str += ch
    my_dict[ch] = my_dict.get(ch, 0) + 1
print(res_str)

# РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ

chars = input("Введите строку, с которой будем работать => ").split()
dict_chars = {}.fromkeys(chars, 0)
print(dict_chars)

for i in chars : 
    print(f"{i}_{dict_chars[i]}" if dict_chars[i] else i, end = " ")
    dict_chars[i] += 1