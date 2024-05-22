import sys
from os import path
import math


def input():
    return sys.stdin.readline().strip()

def solve(n,k,lst):
    modified = [1] * (len(lst)-1)
    for i in range(len(lst)-1):
        if lst[i] < 2 * lst[i+1]:
            modified[i] = 1
        else:
            modified[i] = 0
    i = j = 0
    s = 0
    ans = 0
    while j < len(modified):
        s += modified[j]
        if j - i + 1 < k:
            j += 1
        else:
            
            if s == k:
                ans += 1
            s -= modified[i]
            j += 1
            i += 1
    print(ans)
        
    
    

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,k,lst)
        
    
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()