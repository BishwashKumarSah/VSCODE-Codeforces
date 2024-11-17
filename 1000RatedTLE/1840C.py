import sys
from os import path
import math
from collections import *

#! Link:      https://codeforces.com/problemset/problem/1840/C

# https://www.youtube.com/watch?v=SoZuFp-JbVU&ab_channel=Thinkn%27Code

def input():
    return sys.stdin.readline().strip()


def solve(n, k,q,lst):
    i = 0
    j = 0
    cur = 0
    res = 0
    while j < len(lst):
        if lst[j] <= q:
            cur += 1
            j += 1
        else:
            if cur >= k:
                # no. of ways to pick at least k ball 
                # if total = 5 and at k reaches 5 then total - k + 1
                # so eq = (n * (n + 1) )//2
                eq = (((j - i) - k + 1) * ((j-i) - k + 2)) // 2
                res += eq     
            j += 1
            i = j
            cur = 0
            
    
    if cur >= k:    
        eq = (((j - i) - k + 1) * ((j-i) - k + 2)) // 2
        res += eq  
    print(res)     
    

def main():
    t = int(input())
    for _ in range(t):
        n,k,q = map(int,input().split())
        lst = list(map(int, input().split()))
        
        solve(n,k,q, lst)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()