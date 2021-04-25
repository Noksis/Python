import numpy as np
import pandas as pd
list = ["username","commits","changed_lines","new_files"]
Ans = pd.DataFrame(columns = list)
N = []
f = open('input.txt','r')
df = pd.DataFrame()
df = pd.read_json(f)
df = df.sort_values(by='commit_time')
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
df.reset_index(inplace=True)
for i in range(len(df)):
    Name = df['username'][i]
    Index = Ans.index[Ans['username'] == Name].tolist()
    if not Index:
        Index = len(Ans)
        Ans.loc[Index,'username'] = Name
        Ans.loc[Index,'commits'] = int(0)
        Ans.loc[Index,'changed_lines'] = int(0)
        Ans.loc[Index,'new_files'] = int(0)
        Index = Ans.index[Ans['username'] == Name].tolist()

    Ans.loc[Index, "commits"] += 1

    for k in df.loc[i,'files']:
        Ans.loc[Index, "changed_lines"] += k["changed_lines"]
        if (k['name'] not in N):
            N.append(k['name'])
            Ans.loc[Index,"new_files"] += 1
Ans = Ans.sort_values('username')


Ans = Ans.astype({'username': 'str'})
Ans = Ans.astype({'commits': 'int'})
Ans = Ans.astype({'changed_lines': 'int'})
Ans = Ans.astype({'new_files': 'int'})

print(Ans.to_string(index=False))
