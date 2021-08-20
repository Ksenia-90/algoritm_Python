#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random
N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0:
        if index == -1 or arr[i] > arr[index]:
            index = i
    i += 1


print(f'значение: {arr[index]}, позиция:{index}')
