import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,arr):
    print(-(sum(arr)))

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int,input().split()))
        solve(n,arr)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        