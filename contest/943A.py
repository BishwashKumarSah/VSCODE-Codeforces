import sys
import collections
import math

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n):
    ans = float("-inf")
    for i in range(1,n):
        if math.gcd(n,i) + i > ans:
            ans = i 
    print(ans)
    
    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()