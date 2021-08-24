# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import cProfile
import sys
from random import random


def calc(n):
    array = []
    for i in range(n):
        array.append(int(random() * 100))
    first = sys.maxsize
    second = first
    for i in range(n):
        if array[i] <= second:
            second = array[i]
            if second < first:
                first, second = second, first

#cProfile. run ('calc(100)')
'''
204 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_var_1.py:8(calc)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      100    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
'''
#cProfile. run ('calc(1000)')
'''
2004 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_var_1.py:8(calc)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

'''

#
#cProfile. run ('calc(10000)')
'''
     20004 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 task_1_var_1.py:8(calc)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects} 
'''
#" "task_1_var_1.calc(100)"
#1000 loops, best of 5: 14 usec per loop

#" "task_1_var_1.calc(1000)"
#1000 loops, best of 5: 141 usec per loop

#" "task_1_var_1.calc(10000)"
#1000 loops, best of 5: 1.43 msec per loop

