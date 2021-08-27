#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
#Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].



from collections import deque, ChainMap

dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
        "D": 13, "E": 14, "F": 15}

dict_reverse = {v: k for k, v in dict.items()}

variants = ChainMap(dict, dict_reverse)

first_deque = deque(input('Введите первое число в шестнадцатиричном формате:'))
second_deque = deque(input('Введите второе число в шестнадцатиричном формате:'))
operator = input("Введите оператор: ")


if operator == "+":
    diff = len(first_deque) - len(second_deque)
    if diff > 0:
        for i in range(diff):
            second_deque.appendleft("0")
    elif diff < 0:
        for i in range(diff * -1):
            first_deque.appendleft("0")

    first = list(first_deque)
    second = list(second_deque)

    result_deque = deque()

    in_the_mind = 0
    count_item = len(variants) / 2
    for i in reversed(range(len(first))):
        pos_first = variants.get(first[i])
        pos_second = variants.get(second[i])
        sum_position = pos_first + pos_second + in_the_mind
        if sum_position > count_item:
            sum_position = sum_position - count_item
            if sum_position >= count_item:
                sum_position = sum_position - count_item + 1
                result_deque.append(variants[count_item - 1])
            in_the_mind = in_the_mind + 1
        else:
            in_the_mind = 0

        result_deque.append(variants[sum_position])

    res = list(reversed(result_deque))
    print(res)

elif operator == "*":
    result = deque()
    diff = deque([deque() for _ in range(len(second_deque))])

    for i in range(len(second_deque)):
        m = dict[second_deque.pop()]

        for j in range(len(first_deque) - 1, -1, -1):
            diff[i].appendleft(m * variants[first_deque[j]])

        for _ in range(i):
            diff[i].append(0)

    transfer = 0

    for _ in range(len(diff[-1])):
        res = transfer

        for i in range(len(diff)):
            if diff[i]:
                res += diff[i].pop()

        if res < 16:
            result.appendleft(dict_reverse[res])

        else:
            result.appendleft(dict_reverse[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(dict_reverse[transfer])
    print(list(result))
