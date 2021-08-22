#3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

from random import *
#зальём "исходный массив"
main_array=[]
for i in  range(0,20):
    main_array.append(randint(0,100))
print(f'Исходный массив         : {main_array}')

max_c=max(main_array)
min_c=min(main_array)

main_array[main_array.index(max(main_array))]=min_c
main_array[main_array.index(min(main_array))]=max_c

print(f'Преобразованный массив  : {main_array}')