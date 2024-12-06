import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n):
    lst = list(map(int,n))
    for i in range(1,len(lst)):
        if (lst[i] == 0) or (lst[i] - 1 <= lst[i-1]):
            continue
        cur = i
        while cur - 1 >= 0 and lst[cur] - 1 > lst[cur-1]:
            lst[cur],lst[cur-1] = lst[cur-1],lst[cur]-1
            cur -= 1
    return "".join(map(str,lst))
    

def main():
    t = int(input())
    for _ in range(t):
        n = input()
        print(solve(n))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()