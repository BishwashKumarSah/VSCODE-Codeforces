import sys
from os import path
import math

def input():
    return  sys.stdin.readline().rstrip("\r\n")
    

def solve(n,m,k):
    if (m == n and k == m - 1) or  k == m or k > m:
        print("NO")
                 
    else:
        print("YES")
    
    
def main():
    t = int(input())
    while t > 0:
        n,m,k = map(int,input().split())
        solve(n,m,k )
        t -= 1
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()