#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не меньше медианы, в другой –
# не больше медианы. Задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint, random

# Возьмём сортировку выбором
def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            # Выбор наименьшего значения
            if array[j] < array[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        array[minimum], array[i] = array[i], array[minimum]

    return array

# зададми массив
main_array=[]
for i in range(2*int(random()*15)+1):
    main_array.append(randint(-100,100))

print(f'Исходный  массив: {main_array}')
print(f'После сортировки: {selection_sort(main_array)}')
print(f'Таким образом, медианой является {len(main_array)//2} элемент, равный {main_array[len(main_array)//2]}')