import sys
from os import path
import math


def input():
    return sys.stdin.readline().strip()

def solve(n,s,lst):
    i = j = 0
    ans = float("inf")
    val = 0
    while j < len(lst):
        val += lst[j]
        while i <= j and val > s:
            val -= lst[i]
            i += 1
        if val == s:
            ans = min(ans,len(lst) - (j-i+1))
        j += 1
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
   
    
    
def main():
    t = int(input())
    while t > 0:
        n,s = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,s,lst)
        t -= 1
        
    
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()