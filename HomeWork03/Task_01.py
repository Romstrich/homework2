#1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

partial=[]

for divisor in range(2,10):
    partial.append(0)
    for divisible in range(2,100):
        if divisible % divisor==0:
            partial[divisor-2]+=1

print("В диапазоне от 2 до 99\nчисе кратных:")
for i in range(0,8):
    print(f'{i+2}   {partial[i]} штук')