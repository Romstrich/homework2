#Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.


import cProfile

from random import *

def my_function1():
    matrix=[]
    min_array=[]

    for j in range(4):
        matrix.append([])
        for i in range(4):
            matrix[j].append(randint(0,100))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:4}',end=',')
        print()

    for j in range(len(matrix)):
        min_array.append(min([(lambda i: matrix[i][j])(i) for i in range(len(matrix[j]))]))

    print('Максимальный элемент среди минимальных элементов столбцов матрицы: ',max(min_array))
    return 0

def my_function2():
    matrix=[]
    min_array=[]

    for j in range(4):
        matrix.append([])
        for i in range(4):
            matrix[j].append(randint(-100,100))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:4}',end=',')
        print()

    for j in range(len(matrix)):
        min_array.append(min([(lambda i: matrix[i][j])(i) for i in range(len(matrix[j]))]))

    print('Максимальный элемент среди минимальных элементов столбцов матрицы: ',max(min_array))
    return 0

def main1():
    my_function1()

def main2():
    my_function2()

cProfile.run('main1()')
cProfile.run('main2()')

# 58,  68,  15,  35,
#   60,  50,  88,  33,
#   34,  63,   7,  18,
#   40,  39,  88,  12,
# Максимальный элемент среди минимальных элементов столбцов матрицы:  39
#          166 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 Task_04_01.py:10(my_function1)
#        16    0.000    0.000    0.000    0.000 Task_04_01.py:25(<lambda>)
#         4    0.000    0.000    0.000    0.000 Task_04_01.py:25(<listcomp>)
#         1    0.000    0.000    0.001    0.001 Task_04_01.py:50(main1)
#        16    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
#        16    0.000    0.000    0.000    0.000 random.py:291(randrange)
#        16    0.000    0.000    0.000    0.000 random.py:335(randint)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        21    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        16    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        17    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#  -42, -24,   9, -76,
#   74, -27,  35,  29,
#  -56, -22, -86,  68,
#  -42,  70, -75,  74,
# Максимальный элемент среди минимальных элементов столбцов матрицы:  -27
#          168 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_04_01.py:30(my_function2)
#        16    0.000    0.000    0.000    0.000 Task_04_01.py:45(<lambda>)
#         4    0.000    0.000    0.000    0.000 Task_04_01.py:45(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Task_04_01.py:53(main2)
#        16    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
#        16    0.000    0.000    0.000    0.000 random.py:291(randrange)
#        16    0.000    0.000    0.000    0.000 random.py:335(randint)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        21    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        16    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        19    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#
# Process finished with exit code 0
