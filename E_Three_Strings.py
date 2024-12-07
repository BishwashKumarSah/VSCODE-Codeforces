import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(a, b,c):
    cache = {}
    def recu(i,j):
        if i >= len(a) and j >= len(b):
            return 0
        
        if (i,j) in cache:
            return cache[(i,j)]
        k = i + j
        res = float("inf")
        if i < len(a):
            if c[k] != a[i]:
                res = min(res,1+recu(i+1,j))
            else:
                res = min(res,recu(i+1,j))
        if j < len(b):
            if c[k] != b[j]:
                res = min(res,1 + recu(i,j+1))
            else:
                res = min(res,recu(i,j+1))
        cache[(i,j)] = res
        return cache[(i,j)]
    return recu(0,0)
            
    

def main():
    t = int(input())
    for _ in range(t):
       a = input()
       b = input()
       c = input()
       print(solve(a, b, c))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()