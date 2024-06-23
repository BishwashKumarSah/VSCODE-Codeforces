import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(r,c,matrix):
    for i in range(r):
        for j in range(len(matrix[0])):
            
            lst = [float("inf"),float("inf"),float("inf"),float("inf")]
            if i - 1 >= 0:
                lst[0] = matrix[i-1][j]
            if j - 1 >=0:    
                lst[1] = matrix[i][j-1]
            if i + 1 < len(matrix):
                lst[2] = matrix[i+1][j]
            if j + 1 < len(matrix[0]):
                lst[3] = matrix[i][j+1]
            flag = True
            maxV = float("-inf")
            for value in lst:
                if value == float("inf"):
                    continue
                else:
                    if value < matrix[i][j]:
                        maxV = max(maxV,value)
                    else:
                        flag = False
                        break
            if flag == False:
                continue
            else:
                matrix[i][j] = maxV
                    
    for data in matrix:
        print(" ".join(map(str,data)))
    

def main():
    t = int(input())
    for _ in range(t):        
        r,c = map(int,input().split())
        matrix = []
        for i in range(r):
            val =list(map(int,input().split()))
            matrix.append(val)        
        solve(r,c,matrix)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()