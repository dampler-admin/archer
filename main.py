import os
from random import random
N = 999999
X = 999999
arr = [0]*N
arr2 = []*X
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(N):
    arr2[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)
print("Ты пидор!")

