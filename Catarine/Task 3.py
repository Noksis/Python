import numpy as np
import pandas as pd

def check (Name, Ax):
    for i in Ax:
        if i[0] == Name:
            return False
    return True


A = ["username","commits","changed_lines","new_files"]
pA = pd.DataFrame(columns = A)
pB = pd.read_json('input.txt')
pB = pB.sort_values(by='commit_time')
pB.reset_index(inplace=True)
Ax = []
for i in range(len(pB)):
    Name = pB.loc[i]['username']
    if check(Name,Ax):
        Ax.append([Name,0,0,0])
    for z in range(len(Ax)):
        if Ax[z][0] == Name:
            Q = z
    for j in pB.loc[i,'files']:
            if (j['name'] not in A):
                A.append(j['name'])
                Ax[Q][3] +=1
            Ax[Q][2] += j["changed_lines"]
    Ax[Q][1] +=1
pA = pd.DataFrame(Ax,columns = ["username","commits","changed_lines","new_files"])
pA = pA.sort_values('username')
print(pA.to_string(index=False))
