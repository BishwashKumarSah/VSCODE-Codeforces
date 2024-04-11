import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,s):
    if len(s) == n:  
        print(s)      
        return 
    solve(n,s = s+"0")
    solve(n,s = s+"1")

def main():
    n = int(input())   
    lst = list(map(int,input().split()))
    solve(n,"")     
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()