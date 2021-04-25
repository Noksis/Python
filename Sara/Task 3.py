import numpy as np
import pandas as pd

def Add_str (Commits,Name):
    new = len(Commits)
    Commits.loc[new,"username"] = Name
    Commits.loc[new,"commits"] = 0
    Commits.loc[new,"changed_lines"] = 0
    Commits.loc[new,"new_files"] = 0
    return 0

Commits = pd.DataFrame(columns = ["username","commits","changed_lines","new_files"])
list = []

JSON = pd.read_json('input.txt')
JSON = JSON.sort_values(by='commit_time')
JSON.reset_index(inplace=True)
size = 100
for i in JSON.index:
    Name = JSON.loc[i]['username']
    i_com = Commits.index[Commits.username == Name].to_list()
    if i_com == []:
        Add_str(Commits,Name)
    i_com = Commits.index[Commits.username == Name].tolist()
    for k in JSON.loc[i,'files']:
        if (k['name'] not in list):
            list.append(k['name'])
            Commits.loc[i_com,"new_files"] = 1 +  Commits.loc[i_com,"new_files"]
        Commits.loc[i_com, "changed_lines"] = k["changed_lines"] + Commits.loc[i_com, "changed_lines"]
    Commits.loc[i_com, "commits"] = 1 + Commits.loc[i_com, "commits"]

Commits = Commits.sort_values('username')
print(Commits.to_string(index=False))
