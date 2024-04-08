import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,cc,d,lst):
    lst.sort()
    firstElement = lst[0]
    res = [[0 for _ in range(n)] for _ in range(n)]
    
    row = len(res)
    col = len(res[0])
    res[0][0] = firstElement
    ans = []
    for r in range(row):
        for c in range(col):
            ans.append(res[r][c])
            if r + 1 < row :
                res[r+1][c] = res[r][c] + cc
                
            if c + 1 < col :
                res[r][c+1] = res[r][c] + d
    ans.sort()
    if ans == lst:
        print("YES")
        return
    else:
        print("NO")
    
    

def main():
    t = int(input())
    while t > 0:
        n,c,d = list(map(int,input().split()))
        lst = list(map(int,input().split()))
        solve(n,c,d,lst)
        t -= 1
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()