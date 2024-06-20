import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    first = lst[0]
    val = -1
    ans = []
    for i in range(1,len(lst)):
        if lst[i] != first:
            val = i+1
            break
    for i in range(1,len(lst)):
        if lst[i] != first:
            ans.append([1,i+1])      
        else:
            if val == -1:
                continue
            ans.append([val,i+1])
    if val == -1:
        print("NO")
        return
    else:
        print("YES")
        for i in ans:
            print(*i)

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        
        solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()