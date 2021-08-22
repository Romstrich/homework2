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
