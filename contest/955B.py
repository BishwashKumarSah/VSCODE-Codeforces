import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n,l,r, lst):
    i = 0
    j = 0
    ans = 0
    s = lst[0]
    while j < len(lst):
        if s >= l and s <= r:
            ans += 1
            j +=1
            i = j
            if i < len(lst):
                s = lst[i]
        elif lst[i] > r:
            j += 1
            i = j
            if i < len(lst):
                s = lst[i]
            
        elif s > r:
            s -= lst[i]
            i += 1
        elif s < r:            
            if j + 1 < len(lst):
                s += lst[j+1]                
                j += 1
            else:
                print(ans)
                return    
   
    print(ans) 
        
    

def main():
    t = int(input())
    for _ in range(t):
        n,l,r = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,l,r, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()