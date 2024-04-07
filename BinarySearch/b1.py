import sys
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = high - (low + high)

def main():
    t = int(input())
    while t > 0:
        arr = list(map(int,input().split()))
        target = int(input())
        solve(arr,target)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()