#Простые числа - Решето Эратосфена

import cProfile
def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
#cProfile. run ('eratosthenes(10)')

'''
 8 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_1.py:3(eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#cProfile. run ('eratosthenes(35)')
'''
15 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_1.py:3(eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#cProfile. run ('eratosthenes(100)')
'''
29 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_1.py:3(eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#cProfile. run ('eratosthenes(500)')

'''
         99 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_1.py:3(eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       95    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

#"task_2_var_1.eratosthenes(10)"
#1000 loops, best of 5: 1.61 usec per loop

#"task_2_var_1.eratosthenes(35)"
#1000 loops, best of 5: 4.43 usec per loop

#"task_2_var_1.eratosthenes(100)"
#1000 loops, best of 5: 10.6 usec per loop

#"task_2_var_1.eratosthenes(500)"
#1000 loops, best of 5: 55.7 usec per loop





