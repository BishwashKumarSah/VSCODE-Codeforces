import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()


def solve(n,k,lst):
    if k == 1:
        for i in range(len(lst)-1):
            if lst[i] <= lst[i+1]:
                continue
            else:
                print("NO")
                return
    print("YES")
    
    

def main():
    t = int(input())
    while t > 0:
        n,k = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,k,lst)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()