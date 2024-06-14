import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(n,arr):
    
    ans = float("inf")
    for i in range(1,len(arr)):
        ans = min(max(arr[i],arr[i-1]),ans)
        
    print(ans-1)
    
            
            
        
    
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