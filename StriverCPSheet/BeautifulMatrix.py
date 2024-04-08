import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(matrix):
    middle = [2,2]
    row = len(matrix)
    col = len(matrix[0])
    val = []
    found = False
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 1:
                val.append(r)
                val.append(c)
                found = True
                break
        if found:
            break
    ans = abs((middle[0] - val[0]))  + abs((middle[1]-val[1]))
    print(ans)      
            
    
    

def main():
    matrix = []
    for i in range(5):
        lst = list(map(int,input().split()))
        matrix.append(lst)
    solve(matrix)
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()