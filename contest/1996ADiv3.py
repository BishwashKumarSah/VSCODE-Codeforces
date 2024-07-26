import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n):
    if n <= 2:
        print(1)
    else:
        if n % 4 == 0:
            print(n//4)
            return 
        else:
            rem = n%4
            total = n//4
            rem_new = rem//2
            print(total + rem_new)
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())         
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()