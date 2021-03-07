arr1 = list(map(str, input().split()))
arr2 = list(map(str, input().split()))

for i in range(len(arr1)):
    arr1[i] = arr1[i].lower()

    if arr1[i][-1] == ',' or arr1[i][-1] == '.':
        arr1[i] = arr1[i][:-1]
arr1.sort()


for i in range(len(arr2)):
    arr2[i] = arr2[i].lower()

    if arr2[i][-1] == ',' or arr2[i][-1] == '.':
        arr2[i] = arr2[i][:-1]
arr2.sort()

if arr1 == arr2:
    print("YES")
else:
    print("NO")
