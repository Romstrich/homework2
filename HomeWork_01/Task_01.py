#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

nomber=input('Введите трёхзначное число: ')
if len(nomber)==3:
    #дописать проверку на числом
    if nomber.isdigit():
        print('Сумма цифр: ', int(nomber[0]) + int(nomber[1]) + int(nomber[2]))
        print('Произведение цифр: ',int(nomber[0])*int(nomber[1])*int(nomber[2]))
    else:
        print('Не похоже на число')
else:
    print('Неверная длина ввода')