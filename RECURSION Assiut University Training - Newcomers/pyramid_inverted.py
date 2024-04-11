import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,s,i):
    if i == 0:
        return
    s1 = s[1:len(s)-1]
    print(" " * (n-i) + s)
    solve(n,s1,i-1)

def main():
    n = int(input())
    # s = "*" * ((n-1) * 2 + 1)  
    s = "*" * (2*n - 1)  
     
    solve(n,s,n)     
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()