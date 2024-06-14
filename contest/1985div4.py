import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(x,y,z,k):
    ans = 0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if k % (i * j) == 0:                               
                m = k // (i*j)   
                if m > z:
                    continue            
                val = (x-i+1) * (y-j+1) * (z-m+1)
                ans = max(ans,val)
                
    print(ans)
                    

def main():        
    t = int(input())
    for _ in range(t):
        x,y,z,k = map(int,input().split())               
        solve(x,y,z,k)
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()