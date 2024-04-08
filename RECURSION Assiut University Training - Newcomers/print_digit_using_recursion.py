import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n):
    if n < 9:
        print(n,end=" ")
        return 
    digit = n % 10
    n = n//10
    solve(n)
    print(digit,end=" ")

def main():
    n = int(input())
    while n > 0:
        a = int(input())
        solve(a)
        n -= 1
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()