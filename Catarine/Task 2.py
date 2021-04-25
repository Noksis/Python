import numpy as np
A = list(map(str,input().split(';')))
B = list(map(str,input().split(';')))
OX = len(A)
OY = len(B[0].split(' '))
X = np.arange(OX*OY).reshape((OX,OY))
Y = np.arange(OX*OY).reshape((OX,OY))
Z = 0
for i in range(OX):  
    X[i] = A[i].split(' ')
    Y[i] = B[i].split(' ')
for x in range(OX):
    for y in range(OY):
        Q = min(OX-x,OY-y)
        R = Q + 1
        for k in range(1,R):
            X1 = np.hsplit(X,(y,y+k))
            X2 = np.vsplit(X1[1],(x,x+k))
            if (abs(np.linalg.det(X2[1])-Y[x][y]) < 0.0001):
                Z += 1
if Z == 1:
    print("True")
else:
    print("False")
