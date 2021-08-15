#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
nomber=int(input('Введите количество элементов: '))
start=1
summ=0
for i in range(nomber):

    if i%2==1:
        summ-=start
    else:
        summ+=start
    #print(f'{start}     {summ}')
    start/=2

print(summ)