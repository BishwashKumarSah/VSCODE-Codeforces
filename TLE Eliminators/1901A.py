import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()


def solve(n,k,lst):
    ans = [lst[0]]
    for i in range(1,len(lst)):
        ans.append(lst[i]-lst[i-1])
    ans.append(2 * (k - lst[-1]))
    print(max(ans))
        
    

def main():
    t = int(input())
    while t > 0:
        n,k = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,k,lst)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()