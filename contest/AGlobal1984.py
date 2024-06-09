import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n):
    s = str(n)
    for ind,v in enumerate(s):
        val = int(v)
        if ind == 0:
            if val > 1:
                print("NO")
                return
        if ind == len(s) -1:
            if val >=0 and val <= 8:
                continue
            else:
                print("NO")
                return
        else:
            if val > 0 and val <= 9:
                continue
            else:
                print("NO")
                return
    print("YES")
    
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