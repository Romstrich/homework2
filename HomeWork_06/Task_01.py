#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.
#Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов
# кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев
# к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

from sys import getsizeof
import __main__


#1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

partial=[]

for divisor in range(2,10):
    partial.append(0)
    for divisible in range(2,100):
        if divisible % divisor==0:
            partial[divisor-2]+=1

print("В диапазоне от 2 до 99\nчисел кратных:")
for i in range(0,8):
    print(f'{i+2}   {partial[i]} штук')



#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
from random import *
#зальём "исходный массив"
main_array=[]
for i in  range(0,20):
    main_array.append(randint(0,100))
print(f'Исходный массив: {main_array}')
iter_a=sorted([main_array.index(min(main_array)),main_array.index(max(main_array))])
summa=0
for i in range(iter_a[0]+1,iter_a[1]-1):
    summa+=main_array[i]
print('Сумма элементов, находящихся между минимальным и максимальным элементами: ',summa)

#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import *

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

print('Размеры переменных:')
print(getsizeof(partial))
print(getsizeof(divisor))
print(getsizeof(divisible))
print(getsizeof(summa))
print(getsizeof(main_array))
print(getsizeof(i))
print(getsizeof(j))
print(getsizeof(k))

# Размеры переменных:
# 120       partial
# 28        divisor
# 28        divisible
# 28        summa
# 248
# 28
# 28