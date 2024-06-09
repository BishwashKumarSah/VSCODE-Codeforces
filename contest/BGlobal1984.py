import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,lst):
    c = 0
    
    for i in range(len(lst)): 
        if lst[i] == 0:
            if i == len(lst) - 1:
                c = abs(c)            
                continue       
        if lst[i] < 0:            
            c += lst[i]
        else:
            c = abs(c)
            c += lst[i]
    
    print(abs(c))
        
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()