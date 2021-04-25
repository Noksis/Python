import numpy as np
data = []
anw = 0

data = list(map(str,input().split(';')))
size1 = len(data)
size2 = len(data[0].split(' '))
X = np.zeros((size1,size2),dtype = int)
for i in range(size1):
    X[i] = data[i].split(' ')

data = list(map(str,input().split(';')))
size1 = len(data)
size2 = len(data[0].split(' '))
Y = np.zeros((size1,size2),dtype = int)
for i in range(size1):
    Y[i] = data[i].split(' ')

for i in range(size1):
    for j in range(size2):
        for k in range(1,min((size1 - i),(size2 - j))+1):
            N = np.hsplit(X,(j,j+k))
            M = np.vsplit(N[1],(i,i+k))
            D = np.linalg.det(M[1])
            if (abs(D -Y[i][j]) < 0.000000001):
                anw = 1
                break
        if anw == 1:
            break
    if anw == 1:
         break
if anw == 1:
    print("True")
else:
    print("False")
