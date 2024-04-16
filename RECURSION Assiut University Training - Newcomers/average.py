
import sys
from os import path
import math

input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve(i,n,s,average):    
    if i == n:
        print(format(average/n, '.6f'))
        return     
   
    return solve(i+1,n,s,average+s[i])    
  
def main():        
    n = int(input())
    s = list(map(int,input().split()))   
    
    solve(0,n,s,0) 
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()