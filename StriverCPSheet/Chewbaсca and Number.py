import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()


def solve(s):
    ans = ""
    for ind,i in enumerate(str(s)):  
        if ind == 0 and int(i) == 9:
            ans += i
            continue    
        ans += str(min(9-int(i),int(i)))
    
    print(int(ans))
    

def main():
    s = int(input())
    solve(s)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()