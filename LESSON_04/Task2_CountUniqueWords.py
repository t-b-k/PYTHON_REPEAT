"""
ЗАДАЧА 2. 
Пользователь вводит строку текста. 
Словом считается любая последовательность идущих подряд непробельных символов. 
Слова разделены одним или бОльшим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте. 
"""

words_map = {}
words_list = ("She sells sea shells on the sea shore The shells that she sells are sea shells \
              I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells \
              are sea shore shells").lower().split(" ")

#words_list = input().split(" ")
print(words_list)
words_set = set(words_list)
print(len(words_set))
