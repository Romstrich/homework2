#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
#nomber_range=[]
max_summ=0
max_k=0
while 1:
    nomber=input('Введите натуральное число: ')
    if int(nomber)>=0:
        #nomber_range.append(nomber)
        summ=0
        for i in nomber:
            summ+=int(i)
        if summ>max_summ:
            max_summ=summ
            max_k=nomber
    else:
        print('Это не натуральное число')
        break
print(f'{max_k}, {max_summ}')