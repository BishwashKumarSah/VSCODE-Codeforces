import sys
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(s):
    upperCaseCount = 0
    lowerCaseCount = 0
    for c in s:
        if c.isupper():
            upperCaseCount += 1
        elif c.islower():
            lowerCaseCount += 1
    if upperCaseCount > lowerCaseCount:
        s = s.upper()
        print(s)
    else:
        s = s.lower()
        print(s)

def main():
    s = input()
    solve(s)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()