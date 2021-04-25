import numpy as np
import pandas as pd
col = ["person", "links_count"]
Net = pd.DataFrame(columns=col)
f = open('input.txt','r')
Data = []
Data = f.read()
f.close()
Data = Data.replace('\n', '\t')
D = Data.split('\t')
for i in range(0,len(D),1):
    index = Net.index[Net['person'] == D[i]].tolist()
    if not index:
        index = len(Net)
        Net.loc[index,"person"] = D[i]
        Net.loc[index,"links_count"] = 0
        index = Net.index[Net['person'] == D[i]].tolist()
    Net.loc[index,"links_count"] += 1

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)


Net = Net.sort_values(by = ["links_count", "person"], ascending = [0,1])
Net = Net[:5]


Net = Net.astype({'links_count': 'int'})
Net = Net.astype({'person': 'str'})

print(Net.to_string(index=False))
