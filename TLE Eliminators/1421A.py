import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(a,b):
    ans = 0
    for i in range(32):
        if a & (1 << i) and b & ( 1 << i) : 
                  
            ans |= (1 << i)
            
    
    print((a ^ ans) + (b ^ ans))
            
    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
               
        solve(a,b)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()