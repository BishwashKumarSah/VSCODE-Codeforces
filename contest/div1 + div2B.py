import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    arr = []
    stack = []
    for i in lst:
        if stack and stack[-1] > i:
            arr.append(stack[-1] - i)
            stack.append(stack[-1])
            continue
        stack.append(i)
    
    ans = 0
    maxV = 0
    arr.sort()
    n = len(arr)   
    for i in range(len(arr)):
        if arr[i] - maxV <=0 :
            continue
        rem = arr[i] - maxV
        maxV += rem
        r_gap = ((n - i  + 1) * rem )
        ans += r_gap
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