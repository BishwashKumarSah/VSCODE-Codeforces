import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n):
    if n == 2 or n == 3:
        print(-1)
        return 
    
    if n == 5:
        print(*[1,3,5,4,2])
    
    lst = [0] * 2000000    
    nn = len(lst)
    for i in range(2,nn):
        if lst[i] > 0:
            continue                     
        for j in range(i + 2,nn,)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())        
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()