# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import cProfile
import sys
from random import random

def calc(n):
    array = []
    for i in range(n):
        array.append(int(random() * 100))
    array.sort()
    first = array[0]
    second = array[1]
    print(f'first: {first}')
    print(f'second: {second}')


#cProfile. run ('calc(100)')
'''
207 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_var_3.py:7(calc)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      100    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
'''
#cProfile. run('calc(1000)')
'''
2007 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 task_1_var_3.py:7(calc)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}

'''
#cProfile. run('calc(10000)')
'''
20007 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.004    0.004    0.007    0.007 task_1_var_3.py:7(calc)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}
        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}
'''
#" "task_1_var_2.calc(100)"
#1000 loops, best of 5: 35.4 usec per loop

#" "task_1_var_2.calc(1000)"
#1000 loops, best of 5: 200 usec per loop

#" "task_1_var_2.calc(10000)"
#1000 loops, best of 5: 1.82 msec per loop



