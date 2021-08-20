# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import sys
from random import random

N = 10
array = []
for i in range(N):
    array.append(int(random() * 100))
    print("%3d" % array[i], end='')
print()

first = sys.maxsize
second = first
for i in range(N):
    if array[i] <= second:
        second = array[i]
        if second < first:
            first, second = second, first

print(f'first: {first}')
print(f'second: {second}')


