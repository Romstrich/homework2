#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import *
#зальём "исходный массив"
main_array=[]
for i in  range(0,20):
    main_array.append(randint(-100,100))
print(f'Исходный массив: {main_array}')
print(f'Наиболее отрицательное число: {min(main_array)}, индекс:{main_array.index(min(main_array))}')
  #  for i in range(len(main_array)):
