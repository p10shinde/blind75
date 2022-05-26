
# n -> number of eggs
# k -> number of floors
import sys


def eggDrop(n, k):
    if k == 0 or k == 1:
        return k

    if n == 1:
        return k

    myMin = sys.maxsize
    

    for x in range(1, k+1):
        res = max(eggDrop(n-1, x-1), eggDrop(n, k-x))

        if myMin > res:
            myMin = res
    return myMin + 1

n = 2
k = 10
print(eggDrop(n,k))