#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

index = int(input("Введите номер буквы в английском алфавите: "))

if index > 0 and index <= 26:
    print(string.ascii_lowercase[index - 1])
else:
    print("Такой буквы нет")

