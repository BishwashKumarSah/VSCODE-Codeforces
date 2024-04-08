import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n):
    if n == 1:
        print(n)
        return 
    print(n,end=" ")
    solve(n-1)

def main():
    n = int(input())
    solve(n)
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()