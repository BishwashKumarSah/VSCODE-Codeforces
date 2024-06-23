import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(x,y,z):
    ans = float("inf")
    for i in range(1,11):
        ans = min(ans,abs(x-i)+abs(y-i)+abs(z-i))
    print(ans)
    

def main():
    t = int(input())
    for _ in range(t):
        x,y,z = map(int,input().split())
        solve(x,y,z)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()