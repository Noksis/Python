import numpy as np
import pandas as pd
def input(DF):
    f = open('input.txt','r')
    DF = f.read()
    DF = DF.replace('\t', '\n')
    DF = DF.split('\n')
    Df = f.close()
    return DF



DF = []
DF = input(DF)
Answer = [["0",0]]
check_in = 1
for i in range(0,len(DF),1):
    Name = DF[i]

    for j in Answer:
        if j[0] == Name:
            check_in = 0

    if check_in:
        Answer[len(Answer)-1] = [Name,0]
        Answer.append(['0',0])

    for k in range(len(Answer)):
        if Answer[k][0] == Name:
            Index = k

    Answer[Index][1] += 1
    check_in = 1

DF1 = pd.DataFrame(Answer, columns = ["person", "links_count"])
DF1 = DF1.sort_values(by = ["links_count", "person"], ascending = [0,1])
DF1 = DF1[:5]
print(DF1.to_string(index=False))
