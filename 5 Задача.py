num = int(input())
name = []
author = []
date = []
lek = []

for i in range(num):
    arr1 = [i for i in input().split() if i != "|"]

    name.append(arr1[0].strip(' '))
    author.append(arr1[1].strip(' '))
    date.append(int(arr1[2]))


for i in range(len(name)):
    var = [int(s) for s, elm1 in enumerate(name) if elm1 == name[i]]
    arr2 = []

    for elm1 in var:
        arr2.append((date[elm1], elm1))

    u = arr2[0]

    for elm2 in arr2:
        if elm2 < u:
            u = elm2

    if u[1] == i:
        lek.append("{} - {}".format(author[i], name[i]))

lek.sort()
for i in range (len(lek)):
    print(lek[i])
