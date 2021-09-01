#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

def buble_sort(array):
    # определяем длину массива
    array=array[:]
    length = len(array)
    # Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length - i - 1):
            # Меняем элементы местами
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

main_array=[]

for i in range(20):
    main_array.append(randint(-100,100))

print(f'Исходный  массив: {main_array}')
print(f'После сортировки: {buble_sort(main_array)}')
