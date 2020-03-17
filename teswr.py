import os
p = int(input("Показатель степени: "))
n = int(input("Максимальный предел степени: "))

i = 1
while i**p <= n:
    print(i**p, end=' ')
    i += 1

print("\nПоследнее число, возводимое в степень:", i - 1)
