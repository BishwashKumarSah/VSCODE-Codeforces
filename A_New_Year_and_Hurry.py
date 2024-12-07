import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, m):
    total = 4 * 60
    res = 0
    cur = m
    for i in range(1,n+1):        
        jj = i * 5      
        cur += jj
        if cur > total:
            break
        res += 1
    print(res)  
        
        
    
    

def main():    
    n,m = list(map(int,input().split()))
    solve(n, m)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()