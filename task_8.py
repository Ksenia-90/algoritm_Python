# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num = int(input('Введите число: '))
digit = int(input('Введите искомое число: '))
num_stop = 0
digit_counter = 0
rank = 1

while num_stop < num:
    i = num % (rank * 10) // rank
    if i == digit:
        digit_counter += 1
    num_stop += i * rank
    rank *= 10

print(f'{digit_counter}')
