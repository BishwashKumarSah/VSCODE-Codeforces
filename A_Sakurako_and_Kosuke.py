import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(val):
    cur = 0
    turn = 0
    count = 1
    while abs(cur) <= val:
        i = (2 * count) - 1
        if turn == 0:
            cur += -1 * i
        else:
            cur += i
        if abs(cur) > val:
            if turn == 0:
                return "Sakurako"
            return "Kosuke"
        if turn == 0:
            turn = 1
        else:
            turn = 0
        count += 1
   
        

def main():
    t = int(input())
    for _ in range(t):      
        val = int(input())
        print(solve(val))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()