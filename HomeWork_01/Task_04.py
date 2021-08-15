# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся
# эти символы. Программа должна вывести на экран любой символ алфавита
# от 'a' до 'f' включительно.

from random import *
my_range=input('Введите диапазон целых чисел a,b:')
my_range=my_range.split(',')
if len(my_range)>1:
    my_range=[int(my_range[0]),int(my_range[1])]
    if my_range[1] < my_range[0]:
        print(f'Случайное число из заданного диапазона: {randint(my_range[1], my_range[0])}')
    else:
        print(f'Случайное число из заданного диапазона: {randint(my_range[0],my_range[1])}')

my_range=input('Введите диапазон вещественных чисел a,b:')
my_range=my_range.split(',')
if len(my_range)>1:
    my_range=[float(my_range[0]),float(my_range[1])]
    if my_range[1] < my_range[0]:
        print(f'Случайное число из заданного диапазона: {uniform(my_range[1], my_range[0])}')
    else:
        print(f'Случайное число из заданного диапазона: {uniform(my_range[0],my_range[1])}')

my_range=input('Введите диапазон символов a,b:')
my_range=my_range.split(',')
if len(my_range)>1:
    my_range=[ord(my_range[0]),ord(my_range[1])]
    if my_range[1] < my_range[0]:
        print(f'Случайный символ из заданного диапазона: {chr(randint(my_range[1], my_range[0]))}')
    else:
        print(f'Случайный символ из заданного диапазона: {chr(randint(my_range[0],my_range[1]))}')