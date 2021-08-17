#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
num = int(input('Введите число: '))
num_stop = 0
num_revert = 0
rank = 1

while num_stop < num:
    i = num % (rank * 10) // rank
    num_revert = num_revert * 10 + i
    num_stop += i * rank
    rank *= 10


print(f'{num_revert}')
