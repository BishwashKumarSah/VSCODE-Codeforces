import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(x1,x2,y1,y2):
    if (x1 - y1) * (x2 - y2) > 0:
        print("YES")
        return 
    
    print("NO")
    

def main():
    t = int(input())
    for _ in range(t):       
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        solve(x1,x2,y1,y2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()