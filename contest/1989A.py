import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, a,b):
    if a >= 0 and b >= 0:
        print("YES")
        return
    if a <= 0 and b >= 0:
        print("YES")
    elif a <= 0 and b <= 0:
        if abs(b) >= 2:
            print("NO")
            return
        else:
            print("YES")
            return
    elif a >= 0 and b <= 0:
        if abs(b) >= 2:
            print("NO")
            return
        else:
            print("YES")
            return
    
    

def main():
    
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        solve(n, a,b)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()