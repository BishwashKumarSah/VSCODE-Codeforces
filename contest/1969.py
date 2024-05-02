import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,arr):
    
    for i in arr:
        val = arr[i-1]
        if arr[val-1] == i:
            print(2)
            return
    print(3)
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        solve(n,arr)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()