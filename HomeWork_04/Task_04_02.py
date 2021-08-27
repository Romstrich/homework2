#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
#Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile

def prime_number1(index):
    #будем искать среди нечётных чисел
    #ведём счётчик простых чисел
    counter=1
    #отсечём 1 и 2.
    if index==1:
        return 2
    else:
        prime_array=list(i*2+1 for i in range(index*5))[1:]
        #print(prime_array)
    #создадим список 10хindex(чтоб хватило=)
    #теперь побежим по списку и будем делить
    for i in range(len(prime_array)):
        #берём prime_array i-е
        cutter=0 #отсечка

        for k in range(i//2):
            #print(f'Делим {prime_array[i]} на {prime_array[k]},         {i}, {k}')

            if prime_array[i]%prime_array[k]==0:
                cutter=1
                break;
            else:
                continue

        if cutter==0:
            #print(f'{prime_array[i]} -простое число')
            counter+=1
            if counter==index:
                #print(f'{index}-е простое число: {prime_array[i]}')
                return prime_array[i]



def prime_number(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b

def prime_number2(index):
    n=index
    while len(prime_number(n))!=index:
        n+=1
    return prime_number(n)[index-1]

def main2():
    print(prime_number2(500))

def main1():
    print(prime_number1(500))

cProfile.run("main1()")

cProfile.run("main2()")

# #3571
#          2508 function calls in 0.038 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.038    0.038 <string>:1(<module>)
#      2501    0.001    0.000    0.001    0.000 Task_04_02.py:16(<genexpr>)
#         1    0.000    0.000    0.038    0.038 Task_04_02.py:77(main1)
#         1    0.037    0.037    0.038    0.038 Task_04_02.py:8(prime_number1)
#         1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 3571
#          942091 function calls in 4.126 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.126    4.126 <string>:1(<module>)
#      3074    3.938    0.001    4.101    0.001 Task_04_02.py:42(prime_number)
#         1    0.023    0.023    4.126    4.126 Task_04_02.py:68(prime_number2)
#         1    0.000    0.000    4.126    4.126 Task_04_02.py:74(main2)
#         1    0.000    0.000    4.126    4.126 {built-in method builtins.exec}
#      3073    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#    935938    0.163    0.000    0.163    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0