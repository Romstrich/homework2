#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import *
#зальём "исходный массив"
main_array=[]
for i in  range(0,20):
    main_array.append(randint(0,100))
print(f'Исходный массив: {main_array}')
print(main_array[main_array.index(sorted(main_array)[0])],main_array[main_array.index(sorted(main_array)[1])])