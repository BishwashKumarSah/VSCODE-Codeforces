import sys
import collections
import math
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n):   
    print((1<<20) - 1)
    ans = 0
    for i in range(0,32):
        if n & (1<<i):
            ans += 1
    print(ans)
    
    
def main():        
    n = int(input())
    solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()