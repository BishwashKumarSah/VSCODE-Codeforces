import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    res = 0
    for i in lst:
        nail = i[0]
        h = i[1]
        if nail - h > 0:
            res += 1            
    
    print(res)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = []
        for _ in range(n):
            v = list(map(int,input().split()))
            lst.append(v)
        solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()