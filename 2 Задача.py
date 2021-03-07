arr = list(map(int, input().split()))
i = 0
ind = 0

while i < (len(arr) - 1):
    if (int(arr[i]) + 1) == int(arr[i+1]) and (int(arr[i]) + 2) == int(arr[i+2]):
        ind = i + 1

        while (int(arr[ind]) + 1) == int(arr[ind + 1]):
            ind += 1
            if ind == len(arr) - 1:
                break
        arr = arr[:i+1] + list('-') + arr[ind:]
        i = i + 2

    if i < (len(arr) - 1):
        arr = arr[:i+1] + list(",") + arr[i+1:]
        i += 2

for i in range(len(arr)):
    print(arr[i], end='')
