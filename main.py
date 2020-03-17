import os
from random import random
N = 999999
X = 999999
A = 999999
Z = 999999
Q = 999999
S = 999999
W = 999999
C = 999999
V = 999999
B = 999999
E = 999999
R = 999999
F = 999999
H = 999999
M = 999999
G = 999999
arr = [0]*N
arr1 = [0]*E
arr2 = [0]*X
arr3 = [0]*A
arr4 = [0]*Z
arr5 = [0]*Q
arr6 = [0]*S
arr7 = [0]*W
arr8 = [0]*C
arr9 = [0]*V
arr10 = [0]*B
arr11 = [0]*R
arr12 = [0]*F
arr13 = [0]*H
arr14 = [0]*M
arr15 = [0]*G
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(E):
    arr1[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(X):
    arr2[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(A):
    arr3[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(Z):
    arr4[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(Q):
    arr5[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(S):
    arr6[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(W):
    arr7[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(C):
    arr8[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(V):
    arr9[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(B):
    arr10[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(R):
    arr11[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(F):
    arr12[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(H):
    arr13[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(M):
    arr14[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
for i in range(G):
    arr15[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)

print(arr)
print('Индексы четных элементов: ', even)


