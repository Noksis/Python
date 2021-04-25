import numpy as np
data = []
data = list(map(int,input().split()))
size = len(data)
Toepliz = np.zeros((size, size), dtype = int)
Toepliz[0] = data
for i in range (1,size):
    for j in range (size):
        if (j < i):
            Toepliz[i][j] = Toepliz[0][i-j]
        else:
            Toepliz[i][j] = Toepliz[i-1][j-1]
for i in range(size):
    if (i % 2 == 1):
        Toepliz[i] = Toepliz[i][::-1]
print(Toepliz)
