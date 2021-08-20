#Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import sys
from pprint import pprint
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

print("Максимальный среди минимальных: ", result)
