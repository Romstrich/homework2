#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import OrderedDict

fabrics=OrderedDict()
year_med_profit=0
up_profit=[]
low_profit=[]

fab_no=int(input('Введите, сколько предприятий: '))

for i in range(fab_no):
    fab_name=input(f'ВВедите название {i+1}-го предприятия: ')
    fabrics[fab_name]=[]
    for k in range(4):
        profit=int(input(f'Введите прибыль для {k+1}-го квартала: '))
        fabrics[fab_name].append(profit)
        year_med_profit+=profit

#Среднегодовой по предприятиям...c небольшой условностью
year_med_profit=year_med_profit//fab_no
print(f'\nСреднегодовой доход одного предприятия: {year_med_profit}\n')

for i in fabrics.keys():
    if sum(fabrics[i])>year_med_profit:
        up_profit.append(i)
    elif sum(fabrics[i])<year_med_profit:
        low_profit.append(i)

print('Предприятия с доходом выше общего среднегодового: ')
for i in up_profit:
    print(f'{i}')

print('Предприятия с доходом ниже общего среднегодового: ')
for i in low_profit:
    print(f'{i}')
