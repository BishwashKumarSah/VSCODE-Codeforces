import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    lst.sort()
    val = lst[0]
    res = 0
    for i in range(len(lst)-1):
        if lst[i] + 1 == lst[i+1]:
            continue
        v = lst[i+1] - lst[i] - 1
        res += v
    print(res)

def main():
    
    n = int(input())
    lst = list(map(int, input().split()))
    solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()