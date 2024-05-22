import sys
from os import path
import math


def input():
    return sys.stdin.readline().strip()

def solve(n,s,lst):
    i = j = 0
    sum = 0
    ans = float("inf")
    while j < len(lst):
        sum += lst[j]
        while i <= j and sum > s:
            sum -= lst[i]
            i += 1
        if sum == s:
            ans = min(ans,len(lst) - (j-i+1))
        j += 1
    if ans == float("inf"):
        print(-1)
        return
    print(ans)
        
    

def main():
    t = int(input())
    for _ in range(t):
        n,s = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,s,lst)
        
    
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()