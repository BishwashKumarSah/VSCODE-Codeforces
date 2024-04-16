import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    if n == 1:
        print(len(lst)+1)
        return
    lst.append(n)
    if n % 2 == 0:
        solve(n//2,lst)
    else:
        solve(3*n + 1,lst)
        
        
def main():
    n = int(input())
    solve(n,[])  
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()