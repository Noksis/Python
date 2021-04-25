import numpy as np

V = list(map(int,input().split()))
T = np.empty((len(V), len(V)), dtype = int)
T[0] = V

for y in range (len(V)-1):
    for x in range (len(V)):

        if (x <= y):
            T[y+1][x] = T[0][y+1-x]
        else:
            T[y+1][x] = T[y][x-1]

for i in range(len(V)):

    if (i % 2 == 1):
        T[i] = np.flip(T[i])

print(T)
