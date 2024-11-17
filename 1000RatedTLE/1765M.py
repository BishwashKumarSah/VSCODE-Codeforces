import sys
from os import path
from math import *
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n):
    
    if n % 2 == 0:
        print(*[n//2,n//2])
        return
    
    first = 1
    second = n - 1
    ans = float("inf")
    
    for i in range(2,n):
        if i * i <= n:
            if n % i == 0:
                a = i
                b = n - a
                val = lcm(a,b)
                if val <= ans:
                    ans = val
                    first = a
                    second = b
                a = n//i
                b = n - a
                val = lcm(a,b)
                if val <= ans:
                    ans = val
                    first = a
                    second = b            
        else:
            print(*[first,second])
            return
            
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())        
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()