import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(i,n,lst,ans):
    if i == n:
        print(ans)
        return
    ans = max(lst[i],ans)
    solve(i+1,n,lst,ans)

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    ans = float("-inf")
    solve(0,n,lst,ans)     
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()