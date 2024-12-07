import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    lst = lst[::-1]
    res = []
    cur = 0
    for i in lst:
        if i > cur:
            cur = i
        if cur > 0:
            res.append(1)
            cur -= 1
        else:
            res.append(0)
    res = res[::-1]
    print(*res)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()