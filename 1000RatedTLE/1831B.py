import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

def getDic(lst,dic1):
    i = 0
    j = 0
    count = 0
    while j < len(lst):
        if lst[j] == lst[i]:
            count += 1
            dic1[lst[j]] = max(dic1[lst[j]],count)
            j += 1
        else:
            count = 0
            i = j
    return dic1

def solve(n, lst1,lst2):    
    
    dic1 = getDic(lst1,defaultdict(int))
    dic2 = getDic(lst2,defaultdict(int))
    
    res = 0
    
    for i in dic1:
        if i in dic2:
            val = dic1[i] + dic2[i]
            res = max(res,val)
        else:
            res = max(res,dic1[i])
    for i in dic2:
        if i in dic1:
            val = dic1[i] + dic2[i]
            res = max(res,val)
        else:
            res = max(res,dic2[i])
    print(res)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        solve(n, lst1,lst2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()