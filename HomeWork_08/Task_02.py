#2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq
from collections import Counter,namedtuple

#прикрутим узел
class node(namedtuple("Node",["left","right"])):
    def walk(self,code,acc):
        self.left.walk(code,acc+"0")
        self.right.walk(code,acc+"1")

#прикрутим лист
class leaf(namedtuple("Leaf",["char"])):
    def walk(self,code,acc):
        code[self.char]=acc

def huffman(s):
    #h=[(freq,leaf(ch)) for ch,freq in Counter(s).items()]
    h=[]
    for ch,freq in Counter(s).items():
        h.append((freq,len(h),leaf(ch)))
    heapq.heapify(h)
    count=len(h)
    while len(h)>1:
        #Подастаём из очереди самое меньшее
        freq1,_count1,left=heapq.heappop(h)
        freq2,_count2, right = heapq.heappop(h)
        #Всунем в очередь суммарную пачку
        heapq.heappush(h,(freq1+freq2,count, node(left,right)))
        count+=1
    #Возьмём корень
    [(_freq,count,root)]=h
    code = {}
    root.walk(code,"")



    return code

s=input('Введите строку из трёх слов: ')
code=huffman(s)
encoded="".join(code[char] for char in s)
print(len(code),len(encoded))
for char in sorted(code):
    print(f'{char},{code[char]}')
print('Входящая строка: ',end='')
for i in s:
    print(bin(ord(i))[2:],end='')
print(f'\nВыходная строка: {encoded}')
