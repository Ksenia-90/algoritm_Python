#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

letter_one = input("Введите первую букву: ")
letter_two = input("Введите вторую букву:")

letter_one_index = string.ascii_lowercase.index(letter_one.lower()) + 1
letter_two_index = string.ascii_lowercase.index(letter_two.lower()) + 1

if letter_one_index > letter_two_index:
    print(letter_one_index - letter_two_index - 1)


elif letter_one_index < letter_two_index:
    print(letter_two_index - letter_one_index - 1)

else:
   print ("0")

print(f"Позиция первой буквы: {letter_one_index}")
print(f"Позиция второй буквы: {letter_two_index}")

