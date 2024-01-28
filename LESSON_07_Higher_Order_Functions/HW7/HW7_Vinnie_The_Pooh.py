# Задача. 
# Винни-Пух попросил вас посмотреть, есть ли в его стихах ритм. 
# Сам он считает, что ритм есть, если число слогов (то есть, число гласных букв) 
# в каждой фразе одинаково. 
# Фраза состоит из одного слова или из нескольких слов, разделенных дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение вводится с клавиатуры. 
# В ответе напишите "Парам пам-пам", если ритм есть, и "Пам парам", если ритма нет. 

vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
russian_alphabeth = vowels.union({"б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ф", "х", 
                                 "ц", "ч", "ш", "щ", "ъ", "ь"})

# phrases = input().split(sep=" ")  # Список строк-фраз
# Надо сопоставить этому списку список из количества гласных в этих строках

def is_phrase (phrase) : 
    set_of_letters = set()
    for ch in phrase.lower() : 
        set_of_letters.add(ch)
    print(set_of_letters)
    return set_of_letters.difference(russian_alphabeth)  == {"-"}

def qty_of_syllables(phrase) : 
    result = 1
    for chr in phrase : 
        if chr in vowels : 
            result += 1 
    return result
     
poem = "Союз-нерушимый-республик-сводобных Сплотила-навеки-великая-Русь-Мать"
# poem = input("Покажите ваши стихи: \n")
# list_of_phrases = poem.split()
# print(list_of_phrases)
# is_poem = True
# for phrase in list_of_phrases : 
#     is_poem = is_poem and is_phrase(phrase)
# if is_poem :
#     set_of_syll_qties = set(map(qty_of_syllables, list_of_phrases))
#     if len(set_of_syll_qties) == 1 : 
#         print("Парам пам-пам!")
#     else : 
#         print("Пам парам!")
# else : 
#     print("Это вообще не стихи!")

# РЕШЕНИЕ В СТИЛЕ PYTHON (НА СЕМИНАРЕ): работает неверно!
    
# alp = "аеёиоуыэюя"
# word_sug = poem.split() # считали список фраз
# print(word_sug)
# vowel_letters = [word.count(char) for word in word_sug for char in word if char.lower() in alp]
# print(vowel_letters)
# print(len(set(vowel_letters)))
# if len(set(vowel_letters)) == 1 : 
#     print("Парам-пам-пам!")
# else : 
#     print("Пам-парам!")

# РЕШЕНИЕ В СТИЛЕ PYTHON (НА СЕМИНАРЕ): исправленное!
    
dictionary = "аеёиоуыэюя"
# poem = input().split()
phrases = poem.split() # считали список фраз
print(phrases)
result = [sum([True for j in word if j.lower() in dictionary]) for word in phrases]
print(result)

if all(result) and len(set(result)) == 1 : # all позволяет исключить те стихи, в которых присутствуют фразы без гласных 
    print("Парам-пам-пам!")
else : 
    print("Пам-парам!")


