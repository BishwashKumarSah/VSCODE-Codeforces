import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,a,b):
    if a < b:
        if n % 2 == 0:
            x = n//2
            print(min(a*n,x*b))
        else:
            odd = 1
            x = (n-1)//2
            print(min(n*a,a*odd+b*x))
    else:
        if n % 2 == 0:
            x = n//2
            print(min(a*n,x*b))
        else:
            odd = 1
            x = (n-1)//2
            print(min(n*a,a*odd+b*x))

def main():
    t = int(input())
    while t > 0:
        n,a,b = list(map(int,input().split()))
        solve(n,a,b)
        t -= 1
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()