# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите число: '))
num_stop = 0
even = 0
odd = 0
rank = 1

while num_stop < num:
    i = num % (rank * 10) // rank
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    num_stop += i * rank
    rank *= 10

print(f'четных цифр - {even}, нечетных - {odd} ')
