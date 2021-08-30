#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

import sys
from count import getsizeof
print(sys.version, sys.platform)

# Python 3.7
# OS - 64bit

#Lesson_3
#9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import sys
from random import random

column_size = 2
row_size = 3
matrix = []
for i in range(row_size):
    row_items = []
    for j in range(column_size):
        n = int(random() * 100)
        row_items.append(n)
        print('%4d' % n, end='')
    matrix.append(row_items)
    print()

result = ~sys.maxsize

for column_index in range(column_size):
    min_column_value = sys.maxsize
    for row_index in range(row_size):
        item = matrix[row_index][column_index]
        if item < min_column_value:
            min_column_value = item
    if min_column_value > result:
        result = min_column_value

#print("Максимальный среди минимальных: ", result)

sum_ = 0
var_lst = (result, matrix, row_size, column_size)
for i in var_lst:
    sum_ += getsizeof(i)
print(f'Под переменные задействованно {sum_} байт памяти')

#Под переменные задействованно 436 байт памяти
