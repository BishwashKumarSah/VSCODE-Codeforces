import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()


def solve(s):
    
    st = str(s)
    count = 0
    for c in st:
        if c == "4" or c == "7":
            count += 1
    if count == 4 or count == 7:
        print("YES")
    else:
        print("NO")

def main():
    s = int(input())
    solve(s)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()