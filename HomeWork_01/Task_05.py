#5. Пользователь вводит две буквы. Определить, на каких местах
#   алфавита они стоят и сколько между ними находится букв.

a=input('Введите первую букву: ')
b=input('Введите вторую букву: ')

if ord(b.lower())>ord(a.lower()):
    pass
else:
    a,b=b,a
if ord(b.lower())-ord(a.lower())-1<33:
    print(f"Между буквами '{a}' и '{b}' {ord(b.lower())-ord(a.lower())-1} букв")
else:
    print('Сложно определить. Буквы из разных алфавитов.')

if ord(b)<123:
    print(f"Место букв в алфавите '{a}' - {ord(a)-96}, '{b}' - {ord(b)-96}")
elif ord(a)>1071:
    print(f"Место букв в алфавите '{a}' - {ord(a) - 1071}, '{b}' - {ord(b) - 1071}")
