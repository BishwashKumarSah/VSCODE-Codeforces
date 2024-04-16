
import sys
from os import path
import math

input = lambda: sys.stdin.readline().rstrip("\r\n")
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def solve(n,r,diff):  
    if n == 1 or n == 0:
        return 1
    if r == 0 or r == 1:
        return 1
    if diff == 0 or diff == 1:
        return 1
    first = fact(n)
    second = fact(r)
    third = fact(diff)
    return first//(second*third)

def main():        
    n,r = map(int,input().split())
         
    diff = (n-r)
    ans = solve(n,r,diff) 
    print(ans)
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()