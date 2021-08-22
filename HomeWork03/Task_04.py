#4. Определить, какое число в массиве встречается чаще всего.

from random import *
#зальём "исходный массив"
main_array=[]
for i in  range(0,20):
    main_array.append(randint(0,100))

print(f'Исходный массив: {main_array}')

number = main_array[0]
max_count = 1
for i in range(len(main_array) - 1):
    value = 1
    for k in range(i + 1, len(main_array)):
        if main_array[i] == main_array[k]:
            value += 1
    if value > max_count:
        max_count = value
        num = main_array[i]

if max_count > 1:
    print(max_count, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
# if len(main_array)==len(set(main_array)):
#     print('Нет одинаковых элементов')
#
# print(f'Исходное множество: {set(main_array)}')