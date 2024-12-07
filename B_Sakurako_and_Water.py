import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    res = 0
    ROWS = n
    COLS = n

    for r in range(1):        
        for c in range(COLS):
            if lst[r][c] == 100001:
                continue
            nr = r
            nc = c
            val = 0
            while nr < ROWS and nc < COLS:
                if lst[nr][nc] < 0:
                    val = max(val,abs(lst[nr][nc]))
                    lst[nr][nc] = 100001
                nr += 1
                nc += 1
            res += val
    for r in range(ROWS):        
        for c in range(1):
            if lst[r][c] == 100001:
                continue
            nr = r
            nc = c
            val = 0
            while nr < ROWS and nc < COLS:
                if lst[nr][nc] < 0:
                    val = max(val,abs(lst[nr][nc]))
                    lst[nr][nc] = 100001
                nr += 1
                nc += 1
            res += val
 
    return res

    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = [list(map(int,input().split())) for _ in range(n)]
        print(solve(n, lst))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()