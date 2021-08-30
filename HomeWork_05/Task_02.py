#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

import collections

class hexler():
    def __init__(self,init_nom): #получим строку
        self.hex_dict=('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
        self.value=self.to_hexler(init_nom)

    #в наш тип
    def to_hexler(self,string):
        if type(string)==str:
            # проверим наше число
            value=[]
            for i in string:
                if i.upper() not in self.hex_dict:
                    print('Это не шестнадцатеричное число!!!')
                    value = None
                    break
                # Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
                else:
                    value.append(i.upper())
            return collections.deque(value)#храним, как в условии
        #рудиментарная ветвь условия
        else:
            return None

    #к целому
    def to_int(self):
        #множим по порядку
        k=1
        dec=0
        self.value.reverse()#Урра! воспользовались методом коллекции
        for i in self.value:
            dec+=self.hex_dict.index(i)*k
            k*=16
        self.value.reverse()
        return dec

    # сложим
    def __add__(self, other):
        return hexler(hex(self.to_int()+other.to_int())[2:])

    #перемножим
    def __mul__(self, other):
        return hexler(hex(self.to_int() * other.to_int())[2:])

    # напечатаем:
    def __str__(self):
        return ''.join(self.value)


a=hexler(input('Введите первое шестнадцатеричное число: '))
b=hexler(input('Введите второе шестнадцатеричное число: '))

print(f'шестнадцатиричная сумма: {a+b}')
print(f'шестнадцатиричное произведение: {a*b}')
#Загнать в список
#Преобразование к числу
#Совершение операций
#вывод
