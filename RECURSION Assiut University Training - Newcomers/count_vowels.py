import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(i,s,ans):
    if i == len(s):
        print(ans)
        return
    if s[i] in "aeiouAEIOU":
        ans += 1
    solve(i+1,s,ans)

def main():
    s = input() 
    ans = 0
    solve(0,s,ans)     
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()