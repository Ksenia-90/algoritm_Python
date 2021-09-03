#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

arr = [random.randint(0, 50) for _ in range(10)]

def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    merge_sort(left)
    merge_sort(right)
    n = m = k = 0
    center = [0] * (len(left) + len(right))
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            center[k] = left[n]
            n += 1
        else:
            center[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        center[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        center[k] = right[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = center[i]
    return arr
print('Метод слияния:', merge_sort(arr[:]))

