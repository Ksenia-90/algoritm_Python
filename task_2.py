import sys
from count import getsizeof
print(sys.version, sys.platform)

# Python 3.7
# OS - 64bit

#lesson_3
#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.


array = [8, 3, 15, 6, 4, 2]
result = []

for index, item in enumerate(array):
    if not item % 2:
        result.append(index)

#print(f"Четные числа находятся на позициях: {result}")

sum_ = 0
var_lst = (result, array)
for i in var_lst:
    sum_ += getsizeof(i)
print(f'Под переменные задействованно {sum_} байт памяти')

#Под переменные задействованно 468 байт памяти