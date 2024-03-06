import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,s):
    count = 0
    countEven = 0
    for i in s:
        if i == ".":
            count += 1
            countEven += 1
        else:
            if count >= 3:
                print(2)
                return
            else:
                count = 0          
    if count >= 3:
        print(2)
    else:
        print(countEven)

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        s = input()
        solve(n,s)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()