#!/usr/bin/python3
import sys
sys.setrecursionlimit(2000)
def Calculator(N, refrence):
    if not N in refrence:
        refrence[N] = Calculator(N-1, refrence) + Calculator(N-2, refrence)
    return refrence[N]

def Helper(N):
    refrence = {0:0, 1:1}
    Calculator(N, refrence)
    return list(refrence.values())

N = int(input("Enter the number till which you want to find the Fionacci series: "))
ans = Helper(N)
print(", ".join(str(s) for s in ans))