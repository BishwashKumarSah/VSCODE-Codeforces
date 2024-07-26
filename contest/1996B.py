import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, k,matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    res = []
    for r in range(0,ROWS,k):
        lst = []
        for c in range(0,COLS,k):
            lst.append(matrix[r][c])
        res.append(lst)
    for row in res:
        print(''.join(map(str, row)))
            
    
    

def main():
    t = int(input())
    for _ in range(t):
        n,k = list(map(int,input().split()))
        # matrix = [list(map(int, input().strip().split())) for _ in range(n)]
        matrix = [list(map(int, input().strip())) for _ in range(n)]
        solve(n, k,matrix)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()