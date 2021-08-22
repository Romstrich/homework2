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