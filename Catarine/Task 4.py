import numpy as np
import pandas as pd

def check (Name, Ax):
    for i in Ax:
        if i[0] == Name:
            return False
    return True

col = ["person", "links_count"]
f = open('input.txt','r')
A = []
A = f.read()
f.close()
A = A.replace('\n', '\t')
A = A.split('\t')
B = []
for i in range(0,len(A),1):
    Name = A[i]
    if check(A[i],B):
        B.append([Name,0])
    for z in range(len(B)):
        if B[z][0] == Name:
            Q = z
    B[Q][1] += 1
K = pd.DataFrame(B, columns = col)
K = K.sort_values(by = ["links_count", "person"], ascending = [0,1])
K = K[:5]
print(K.to_string(index=False))
