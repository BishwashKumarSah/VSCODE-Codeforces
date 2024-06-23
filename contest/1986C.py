import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n,m,s,ind,c):
    lst = list(s)
    lstC = list(c)
    SET = set(ind)
    lstC.sort()
    pt = 0
    for i in range(len(lst)):
        val = i + 1
        if val in SET:            
            lst[i] = lstC[pt]
            pt += 1
            
    ans = "".join(lst)
    print(ans)
            
    

def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        s = input()
        ind = list(map(int,input().split()))
        c = input()
        solve(n,m,s,ind,c)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()