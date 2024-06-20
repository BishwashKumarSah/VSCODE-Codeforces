import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, m,lst):
    dic = defaultdict(int)
    for i in lst:
        dic[i%m] += 1
    ans = 0
    if dic[0] >= 1: 
        ans += 1
    for i in range(1,m):
        if dic[i] >= 1:
            if abs(dic[i] - dic[m-i]) <= 1:
                ans += 1
            else:
                ans += (abs(dic[i] - dic[m-i]))
            dic[m - i] = 0
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        lst = list(map(int, input().split()))
        solve(n,m, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()