# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import cProfile
import random
def calc(n):
    a = [random.randint(-100, 100) for _ in range(n)]

    min_1 = min(a)
    if a.count(min_1) == 2:
        print(min_1,' --- 2 times')
    else:
        a.remove(min_1)
        min_2 = min(a)
        #print('*'*15)
        #print(min_1,min_2)

#cProfile. run ('calc(100)')
'''
539 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 task_1_var_2.py:5(calc)
        1    0.000    0.000    0.000    0.000 task_1_var_2.py:6(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

'''
#cProfile. run ('calc(1000)')
'''
5280 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task_1_var_2.py:5(calc)
        1    0.000    0.000    0.002    0.002 task_1_var_2.py:6(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1269    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}


'''
#cProfile. run ('calc(10000)')
'''
 52762 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
    10000    0.006    0.000    0.011    0.000 random.py:200(randrange)
    10000    0.003    0.000    0.014    0.000 random.py:244(randint)
    10000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.018    0.018 task_1_var_2.py:5(calc)
        1    0.003    0.003    0.017    0.017 task_1_var_2.py:6(<listcomp>)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12751    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

'''
#" "task_1_var_2.calc(100)"
#1000 loops, best of 5: 55.5 usec per loop


#" "task_1_var_2.calc(1000)"
#1000 loops, best of 5: 526 usec per loop


#" "task_1_var_2.calc(10000)"
#1000 loops, best of 5: 5.35 msec per loop


