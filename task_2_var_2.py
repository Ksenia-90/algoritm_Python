#Простые числа - Без "Решето Эратосфена"


import cProfile

def not_eratosthenes(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number
#cProfile. run("not_eratosthenes(10)")

'''
13 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_2.py:6(not_eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
#cProfile. run("not_eratosthenes(35)")
'''
      38 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_2.py:6(not_eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       34    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#cProfile. run("not_eratosthenes(100)")
'''
         103 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_var_2.py:6(not_eratosthenes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#cProfile. run("not_eratosthenes(500)")
'''
       503 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.006    0.006    0.006    0.006 task_2_var_2.py:6(not_eratosthenes)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
      499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
#"task_2_var_2.not_eratosthenes(10)"
#1000 loops, best of 5: 3.81 usec per loop

#"task_2_var_2.not_eratosthenes(35)"
#1000 loops, best of 5: 27.7 usec per loop

#"task_2_var_2.not_eratosthenes(100)"
#1000 loops, best of 5: 179 usec per loop

#"task_2_var_2.not_eratosthenes(500)"
#1000 loops, best of 5: 4.46 msec per loop
