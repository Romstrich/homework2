#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix=[]

for j in range(4):
    matrix.append([])
    for i in range(4):
        matrix[j].append(int(input('Веедите число: ')))
    matrix[j].append(sum(matrix[j]))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=',')
    print()