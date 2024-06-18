import sys
from os import path
import math
import collections

def input():
    return sys.stdin.readline().strip()


def solve(n,lst):
    ans = float("-inf")
    for i in range(len(lst)-1):
        val = lst[i] + lst[-1]
        ans = max(val,ans)
    print(ans)
    
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)    
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()