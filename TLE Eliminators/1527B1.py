import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, s):
    count0 = s.count("0")
    if count0 == 1:
        print("BOB")
        return
    
    if count0 % 2 == 0:
        print("BOB")
        return
    print("ALICE")
    
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n, s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()