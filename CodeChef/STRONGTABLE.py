import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    lst.sort()
    ans = 0
    for i in range(len(lst)):
        ans = max(ans,lst[i] * (len(lst) - i))
    print(ans)
    
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()