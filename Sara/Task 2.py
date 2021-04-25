import numpy as np
def F():
    elms = []
    step = 0.000000001
    elms = list(map(str,input().split(';')))
    X = np.empty((len(elms),len(elms[0].split(' '))),dtype = int)
    for i in range(len(elms)):
        X[i] = elms[i].split(' ')

    elms = list(map(str,input().split(';')))
    Y = np.empty((len(elms),len(elms[0].split(' '))),dtype = int)
    for i in range(len(elms)):
        Y[i] = elms[i].split(' ')

    for y in range(len(elms)):
        for x in range(len(elms[0].split(' '))):
            for k in range(1,min((len(elms) - y),(len(elms[0].split(' ')) - x))+1):
                M = np.split(np.split(X,(y,y+k), axis = 0)[1],(x,x+k),axis = 1)
                Determ = np.linalg.det(M[1])
                if abs(Determ -Y[y][x]) < 0.000000001:
                    return "True"
    return "False"

print(F())
