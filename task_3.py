# 3.Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import random

numbers = [random.randint(0, 50) for _ in range(9)]


def median(num):
    half = len(num) // 2
    num.sort()
    if not len(num) % 2:
        return (num[half - 1] + num[half]) / 2
    return num[half]


print('Исходный массив:', numbers)

print('Медиана:', median(numbers[:]))

