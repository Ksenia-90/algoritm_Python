#1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
#Примечание. Решите задачу при помощи построения графа.

number_of_friends= int(input("Введите количество друзей жмущих руку друг другу: "))

graph = []
for i in range(number_of_friends):
    row = [1] * number_of_friends
    row[i] = 0
    graph.append(row)

print(graph)

#количество ребер
handshakes = 0
for row in graph:
    for i in row:
        handshakes += i

handshakes //= 2

print(f"Всего {handshakes} рукопожатий")

