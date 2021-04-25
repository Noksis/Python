import numpy as np
B = list(map(int,input().split(' ')))
W = len(B)
A = np.arange(W*W).reshape((W,W))
for i in range(len(B)):
    A[0][i] = B[i]
for i in range (1,W):
    for j in range (W):
        if (j >= i):
            A[i][j] = A[i-1][j-1]
        if (j < i):
            A[i][j] = A[0][i-j] 
for i in range(W-1):
    if (i % 2 == 0):
        A[i+1] = A[i+1][::-1]
print(A)
