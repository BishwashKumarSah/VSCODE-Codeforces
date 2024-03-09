import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,k,arr):
    lst = set(arr)
    if k in arr:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    while t > 0:
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        solve(n,k,arr)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        