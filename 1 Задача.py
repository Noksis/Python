def solve():
    str1 = str(input())
    str1 = list(str1)

    ind1 = 0
    ind2 = 0
    i = 0

    while ind1 != len(str1):
        while (str1[i:i+2] != list("lo")) and (str1[i:i+2] != list("ke")):
            i += 1
            if i == len(str1):
                return(''.join(str1))

        ind1 = i
        ind2 = i + 1


        if str1[i] == 'l':
            while str1[ind2] == 'o':
                ind2 += 1
            if str1[ind2] == 'l':
                del str1[ind1:ind2+1]
                i = ind1
            else:
                i = ind2

        elif str1[i] == 'k':
            while str1[ind2] == 'e':
                ind2 += 1
            if str1[ind2] == 'k':
                del str1[ind1:ind2+1]
                i = ind1
            else:
                i = ind2

    return(''.join(str1))

return(solve())
