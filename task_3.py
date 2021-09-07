#3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

# Примечания:
# a. граф должен храниться в виде списка стисмежно;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def generate_graph(num):
    new_graph = {}
    for i in range(num):
        new_graph[i] = set(j for j in range(num) if j != i and bool(random.getrandbits(1)))
    return new_graph

graph = generate_graph(5)
print(graph)
dfs(graph, 0)