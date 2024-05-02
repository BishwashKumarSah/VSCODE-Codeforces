import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,s):
    c = 0
    for i in s:
        if i == "U":
            c += 1
    if c % 2 == 0:
        print("NO")
    else:
        print("YES")
    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n,s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()