import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    dic = defaultdict(int)
    for i in range(len(lst)):
        dic[lst[i] - (i+1)] += 1
    ans = 0   
    for i in dic:
        ans += math.comb(dic[i],2)
    print(ans)
    

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