import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()


def solve(m,n):
    c = 0
    while m <= n:
        m = m * 3
        n = n * 2
        c += 1
    print(c)

def main():
    m,n = map(int,input().split())
    solve(m,n)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()