import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

def bs(low,high,target):
    while high - low > 1:
        mid = low + (high - low)//2
        if lst[mid] >= target:
            high = mid
        else:
            low = mid + 1
    if lst[low] >= target:
        return lst[low]
    elif lst[high] >= target:
        return lst[high]
    return -1

def solve(n, c, s):
    global lst
    lst = []
    res = -1
    for i in range(0,len(s)):
        if s[i] == 'g':
            lst.append(i)
   
    
    for i in range(0,len(s)):
        if s[i] == c:
            val = bs(0,len(lst)-1,i)
            if val == -1:
                res = max(res,len(s) - i + lst[0])
            else:
                res = max(res,val - i)
    print(res)
    return
                
    

def main():
    t = int(input())
    for _ in range(t):
        n,c = input().split()
        s = input()
        solve(n, c, s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()