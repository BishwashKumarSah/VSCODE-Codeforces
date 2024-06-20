import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, k):
    A = n
    B = 1    
    if n % 2 == 0:
        if k % n == 0:
            print(n)
            return
        else:
            print(k%n)
            return
    else:
        if k % 3 == 0:
            k += 1
            if k % n == 0:
                print(n)
            else:
                print(k%n)
        else:
            if k % n == 0:
                print(n)
            else:
                print(k%n)
            
            
    
    

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        solve(n, k)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()