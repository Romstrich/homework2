#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
nomber=int(input('Введите цифру: '))
if nomber>9:
    if nomber<0:
        print('Это не цифра!!!')
elif nomber>=0:
    summ=0;
    count=int(input('Сколько чисел будем проверять?  '))
    for i in range(count):
        insert=input(f'Введите {i+1}-е число ')
        if int(insert)>=0:
            for k in insert:
                if int(k)==nomber:
                    summ+=1
        elif int(insert) < 0:
            for k in insert[1:]:
                if int(k) == nomber:
                    summ += 1

print(f'Цивра {nomber} встречается в введённых числах {summ} раз')

