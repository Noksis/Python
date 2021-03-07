from collections import deque
 
def solve ():
    n = int (input())
    playersWins = [0 for i in range (n)]
    playersPower = [0 for i in range (n)]
    k = int (input ())
    current = deque ([i for i in range (n)])
 
    for i in range (n):
        playersPower[i] = int (input ())
    if (n == 1):
        return playersPower[0]
 
    first = current.popleft ()
    second = 0
 
    while (max (playersWins) != k):
        second = current.popleft ()
        if (playersPower[second] > playersPower[first]):
            first, second = second, first
        if (playersPower[first] == max (playersPower)):
            break
        playersWins[first] += 1
        current.append (second)
 
    return (playersPower[first])
 
print (solve ())
